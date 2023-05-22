import multiprocessing

from external.client import YandexWeatherAPI, logger
from schema import ForecastSchema
from tasks import (
    DataFetchingTask,
    DataCalculationTask,
    DataAggregationTask,
    DataAnalyzingTask,
)
from utils import CITIES


def forecast_weather():
    """Анализ погодных условий по городам."""

    cores_count = multiprocessing.cpu_count()
    max_workers = min(32, (cores_count or 1) + 4)

    logger.info('Fetching has started.')
    data_fetching_task = DataFetchingTask(cities=CITIES.keys(), forecast_api=YandexWeatherAPI(), forecast_schema=ForecastSchema)
    raw_data_fetching = data_fetching_task.get_prepared_data(max_workers=max_workers)

    logger.info('Calculation has started.')
    use_cores = cores_count - 1
    pool = multiprocessing.Pool(processes=use_cores)
    data_calculation_task = DataCalculationTask()
    calculated_weathers = pool.map(data_calculation_task.run, raw_data_fetching)

    logger.info('Aggregation has started.')
    data_aggregation_task = DataAggregationTask()
    sort_calculated_stats = data_aggregation_task.run(calculated_weathers)

    logger.info('Analyzing has started.')
    data_analyzing_task = DataAnalyzingTask()
    best_cities = data_analyzing_task.run(sort_calculated_stats)

    return best_cities


if __name__ == "__main__":
    logger.info('Script has started.')
    forecast_weather()
