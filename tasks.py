import csv
import datetime
import statistics
from concurrent.futures import ThreadPoolExecutor
from typing import Any, Iterator, Optional

import consts
from external.client import logger
from schema import ForecastSchema
from utils import ERR_MESSAGE_TEMPLATE


class CityPreparedData:
    """Класс для подготовки данных."""

    def __init__(self) -> None:
        self.prepared_data: dict[datetime.date, dict[str, int]] = {}
        self.avg_condition: Optional[int] = None
        self.avg_temperature: Optional[float] = None

    def put(self, date: datetime.date, good_temperature: int, good_condition: int) -> None:
        self.prepared_data[date] = {'good_temperature': good_temperature, 'good_condition': good_condition}
        self.avg_good_condition = None
        self.avg_good_temperature = None

    @property
    def avg_good_condition(self) -> int:
        if self.avg_good_condition is None:
            self.avg_good_condition = int(statistics.mean([value.get('good_condition') for value in self.prepared_data.values()]))
        return self.avg_good_condition

    @property
    def avg_good_temperature(self) -> float:
        if self.avg_good_temperature is None:
            self.avg_good_temperature = round(statistics.mean([value.get('good_temperature') for value in self.prepared_data.values()]), 1)
        return self.avg_good_temperature

    @property
    def ratio_temperature_and_condition(self):
        return self.avg_good_condition + self.avg_good_temperature

    def __lt__(self, state) -> bool:
        return not state.ratio_temperature_and_condition < self.ratio_temperature_and_condition

    def __eq__(self, state) -> bool:
        return state.ratio_temperature_and_condition == self.ratio_temperature_and_condition


class DataFetchingTask:
    """Класс для получения данных через API."""

    def __init__(self, cities: list[str], forecast_api, forecast_schema) -> None:
        self.cities = cities
        self.forecast_api = forecast_api
        self.forecast_schema = forecast_schema

    def get_prepared_data(self, max_workers=None) -> Iterator[tuple[str, ForecastSchema]]:
        with ThreadPoolExecutor(max_workers=max_workers) as pool:
            return pool.map(self.get_city_prepared_data, self.cities)

    def get_city_prepared_data(self, city) -> tuple[str, ForecastSchema]:
        return city, self.forecast_schema.parse_obj(self.forecast_api.get_forecasting(city))


class DataCalculationTask:
    """Класс для вычисления погодных параметров."""

    def __init__(self) -> None:
        self.good_condition: list[str] = []
        self.good_temperature: list[int] = []
        self.prepared_data = CityPreparedData()

    def run(self, raw_prepared_data: tuple[str, ForecastSchema]) -> tuple[str, CityPreparedData]:
        city, prepared_data = raw_prepared_data
        for data in prepared_data.forecasts:
            self.good_condition = []
            self.good_temperature = []
            for hour in data.hours:
                if consts.START_DAY <= int(hour.hour) <= consts.END_DAY:
                    self.good_temperature.append(int(hour.temp))
                    if hour.condition in consts.GOOD_CONDITION:
                        self.good_condition.append(hour.condition)

            if self.good_temperature:
                self.prepared_data.put(
                    date=datetime.datetime.strptime(data.date, "%Y-%m-%d").date(),
                    good_temperature=int(statistics.mean(self.good_temperature)),
                    good_condition=len(self.good_condition)
                )

        return city, self.prepared_data


class DataAggregationTask:
    """Класс для объединения вычисленных данных."""

    def run(self, calculated_stats: list[tuple[str, CityPreparedData]]) -> list[tuple[str, CityPreparedData]]:
        sorted_calculated_stats = sorted(calculated_stats, reverse=True, key=lambda value: value[1])
        return sorted_calculated_stats


class DataAnalyzingTask:
    """Класс для финального анализа и получения результата."""

    def create_csv_file(self, data: list[list[Any]], headers: list[str]) -> str:
        with open(consts.CSV_FILE, 'w', newline='', encoding='utf-8') as file:
            try:
                writer = csv.writer(file, quotechar='"', quoting=csv.QUOTE_ALL)
                if headers is not None:
                    file.writelines('sep=,' + '\n')
                    writer.writerow(headers)
                for element in data:
                    writer.writerow(element)
                logger.info('Creation file - {}'.format(consts.CSV_FILE))
                return consts.CSV_FILE
            except Exception as error:
                logger.error('Error - {}'.format(error))
                raise Exception(ERR_MESSAGE_TEMPLATE.format(error))

    def get_prepared_data(self, sorted_calculated_stats) -> list[datetime.date]:
        set_data = set()
        for count, calculated_stats in enumerate(sorted_calculated_stats):
            for data in calculated_stats[1].prepared_data.keys():
                set_data.add(data)

        return sorted(list(set_data))

    def write_down_data_to_csv_file(self, sorted_calculated_stats) -> None:
        set_data = self.get_prepared_data(sorted_calculated_stats)
        headers = ['Город/день', '', *[f'{date.day:02}-{date.month:02}' for date in set_data], 'Среднее', 'Рейтинг']

        data = []
        for count, calculated_stats in enumerate(sorted_calculated_stats):
            city, forecast = calculated_stats
            row1: list[Any] = [city, 'Температура, среднее']
            row2: list[Any] = ['', 'Без осадков, часов']

            for data in set_data:
                if exact_forecast := forecast.prepared_data.get(data):
                    row1.append(exact_forecast.get('good_temperature'))
                    row2.append(exact_forecast.get('good_condition'))
                else:
                    row1.append(None)
                    row2.append(None)
            row1.append(forecast.avg_good_temperature)
            row1.append(count + 1)
            row2.append(forecast.avg_good_condition)
            data.append(row1)
            data.append(row2)
        return self.create_csv_file(data=data, headers=headers)

    def run(self, sorted_calculated_stats: list[tuple[str, CityPreparedData]]) -> list[str]:
        self.write_down_data_to_csv_file(sorted_calculated_stats)
        return self.get_cities_with_best_data(sorted_calculated_stats)

    def get_cities_with_best_data(self, sorted_calculated_stats):
        best_city, best_weather = sorted_calculated_stats[0]
        list_of_best_cities = [best_city]
        for city, weather in sorted_calculated_stats[1:]:
            if weather == best_weather:
                list_of_best_cities.append(city)
        return list_of_best_cities
