import datetime

import pytest

from schema import DetailForecastSchema, GeneralForecastSchema, ForecastSchema
from tasks import CityPreparedData


@pytest.fixture()
def prepared_data():
    prepared_data = CityPreparedData()
    prepared_data.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    prepared_data.put(datetime.date(year=2022, month=1, day=2), 9, 9)
    return prepared_data


@pytest.fixture()
def raw_weathers():
    return ('CAIRO',
        ForecastSchema(
            forecasts=[
                GeneralForecastSchema(date='2022-05-26', hours=[
                                                            DetailForecastSchema(hour='0', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='1', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='2', temp=22, condition='clear'),
                                                            DetailForecastSchema(hour='3', temp=21, condition='clear'),
                                                            DetailForecastSchema(hour='4', temp=20, condition='clear'),
                                                            DetailForecastSchema(hour='5', temp=19, condition='clear'),
                                                            DetailForecastSchema(hour='6', temp=20, condition='clear'),
                                                            DetailForecastSchema(hour='7', temp=22, condition='clear'),
                                                            DetailForecastSchema(hour='8', temp=24, condition='clear'),
                                                            DetailForecastSchema(hour='9', temp=27, condition='clear'),
                                                            DetailForecastSchema(hour='10', temp=30, condition='clear'),
                                                            DetailForecastSchema(hour='11', temp=31, condition='clear'),
                                                            DetailForecastSchema(hour='12', temp=32, condition='clear'),
                                                            DetailForecastSchema(hour='13', temp=34, condition='clear'),
                                                            DetailForecastSchema(hour='14', temp=35, condition='clear'),
                                                            DetailForecastSchema(hour='15', temp=35, condition='clear'),
                                                            DetailForecastSchema(hour='16', temp=35, condition='clear'),
                                                            DetailForecastSchema(hour='17', temp=34, condition='clear'),
                                                            DetailForecastSchema(hour='18', temp=33, condition='clear'),
                                                            DetailForecastSchema(hour='19', temp=32, condition='clear'),
                                                            DetailForecastSchema(hour='20', temp=30, condition='clear'),
                                                            DetailForecastSchema(hour='21', temp=29, condition='clear'),
                                                            DetailForecastSchema(hour='22', temp=27, condition='clear'),
                                                            DetailForecastSchema(hour='23', temp=26, condition='clear')
                                                        ]
                ),
                GeneralForecastSchema(date='2022-05-27', hours=[
                                                            DetailForecastSchema(hour='0', temp=25, condition='clear'),
                                                            DetailForecastSchema(hour='1', temp=24, condition='clear'),
                                                            DetailForecastSchema(hour='2', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='3', temp=22, condition='clear'),
                                                            DetailForecastSchema(hour='4', temp=22, condition='clear'),
                                                            DetailForecastSchema(hour='5', temp=21, condition='clear'),
                                                            DetailForecastSchema(hour='6', temp=21, condition='clear'),
                                                            DetailForecastSchema(hour='7', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='8', temp=25, condition='clear'),
                                                            DetailForecastSchema(hour='9', temp=28, condition='clear'),
                                                            DetailForecastSchema(hour='10', temp=29, condition='clear'),
                                                            DetailForecastSchema(hour='11', temp=31, condition='clear'),
                                                            DetailForecastSchema(hour='12', temp=33, condition='clear'),
                                                            DetailForecastSchema(hour='13', temp=34, condition='clear'),
                                                            DetailForecastSchema(hour='14', temp=36, condition='clear'),
                                                            DetailForecastSchema(hour='15', temp=36, condition='clear'),
                                                            DetailForecastSchema(hour='16', temp=36, condition='clear'),
                                                            DetailForecastSchema(hour='17', temp=35, condition='clear'),
                                                            DetailForecastSchema(hour='18', temp=34, condition='clear'),
                                                            DetailForecastSchema(hour='19', temp=33, condition='clear'),
                                                            DetailForecastSchema(hour='20', temp=31, condition='clear'),
                                                            DetailForecastSchema(hour='21', temp=30, condition='clear'),
                                                            DetailForecastSchema(hour='22', temp=28, condition='clear'),
                                                            DetailForecastSchema(hour='23', temp=27, condition='clear')
                                                        ]
                ),
                GeneralForecastSchema(date='2022-05-28', hours=[
                                                            DetailForecastSchema(hour='0', temp=26, condition='clear'),
                                                            DetailForecastSchema(hour='1', temp=25, condition='clear'),
                                                            DetailForecastSchema(hour='2', temp=24, condition='clear'),
                                                            DetailForecastSchema(hour='3', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='4', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='5', temp=22, condition='clear'),
                                                            DetailForecastSchema(hour='6', temp=22, condition='clear'),
                                                            DetailForecastSchema(hour='7', temp=24, condition='clear'),
                                                            DetailForecastSchema(hour='8', temp=26, condition='clear'),
                                                            DetailForecastSchema(hour='9', temp=28, condition='clear'),
                                                            DetailForecastSchema(hour='10', temp=31, condition='clear'),
                                                            DetailForecastSchema(hour='11', temp=33, condition='clear'),
                                                            DetailForecastSchema(hour='12', temp=34, condition='clear'),
                                                            DetailForecastSchema(hour='13', temp=36, condition='clear'),
                                                            DetailForecastSchema(hour='14', temp=36, condition='clear'),
                                                            DetailForecastSchema(hour='15', temp=37, condition='clear'),
                                                            DetailForecastSchema(hour='16', temp=37, condition='clear'),
                                                            DetailForecastSchema(hour='17', temp=37, condition='clear'),
                                                            DetailForecastSchema(hour='18', temp=36, condition='clear'),
                                                            DetailForecastSchema(hour='19', temp=34, condition='clear'),
                                                            DetailForecastSchema(hour='20', temp=33, condition='clear'),
                                                            DetailForecastSchema(hour='21', temp=31, condition='clear'),
                                                            DetailForecastSchema(hour='22', temp=29, condition='clear'),
                                                            DetailForecastSchema(hour='23', temp=28, condition='clear')
                                                        ]
                ),
                GeneralForecastSchema(date='2022-05-29', hours=[
                                                            DetailForecastSchema(hour='0', temp=27, condition='clear'),
                                                            DetailForecastSchema(hour='1', temp=26, condition='clear'),
                                                            DetailForecastSchema(hour='2', temp=25, condition='clear'),
                                                            DetailForecastSchema(hour='3', temp=24, condition='clear'),
                                                            DetailForecastSchema(hour='4', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='5', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='6', temp=23, condition='clear'),
                                                            DetailForecastSchema(hour='7', temp=26, condition='clear'),
                                                            DetailForecastSchema(hour='8', temp=28, condition='clear')
                                                        ]
                ),
                GeneralForecastSchema(date='2022-05-30', hours=[])
            ]
        )
    )


@pytest.fixture()
def calculation_weather_statistics():
    prepared_data_1 = CityPreparedData()
    prepared_data_1.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    prepared_data_1.put(datetime.date(year=2022, month=1, day=2), 9, 9)

    prepared_data_2 = CityPreparedData()
    prepared_data_2.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    prepared_data_2.put(datetime.date(year=2022, month=1, day=2), 9, 9)
    return [('MOSCOW', prepared_data_1), ('PARIS', prepared_data_2),]


@pytest.fixture()
def sort_calculation_weather_statistics():
    prepared_data_1 = CityPreparedData()
    prepared_data_1.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    prepared_data_1.put(datetime.date(year=2022, month=1, day=2), 9, 9)

    prepared_data_2 = CityPreparedData()
    prepared_data_2.put(datetime.date(year=2022, month=1, day=1), 6, 6)
    prepared_data_2.put(datetime.date(year=2022, month=1, day=1), 9, 9)
    return [('PARIS', prepared_data_2), ('MOSCOW', prepared_data_1),]
