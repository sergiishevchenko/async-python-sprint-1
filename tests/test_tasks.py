import datetime

from tasks import CityPreparedData, DataAggregationTask, DataAnalyzingTask, DataCalculationTask


class TestCalculatedCity:

    def test_put(self):
        prepared_data = CityPreparedData()
        prepared_data.put(datetime.date(year=2022, month=1, day=1), 6, 6)

        assert prepared_data.prepared_data == {datetime.date(year=2022, month=1, day=1): {'good_temperature': 6, 'good_condition': 6}}

    def test_average_good_condition(self, prepared_data):
        assert prepared_data.avg_good_condition == 7

    def test_average_good_temps(self, prepared_data):
        assert prepared_data.avg_good_temperature == 7.5


# class TestDataFetchingTask


class TestDataCalculationTask:

    def test_run(self, raw_weathers):
        data_calculation_task = DataCalculationTask()
        city, calculated_weathers = data_calculation_task.run(raw_weathers)

        assert city == raw_weathers[0]
        assert calculated_weathers.avg_good_condition == 11
        assert calculated_weathers.avg_good_temperature == 33
        assert calculated_weathers.prepared_data.get(datetime.date(year=2022, month=5, day=26)).get('good_temperature') == 32
        assert calculated_weathers.prepared_data.get(datetime.date(year=2022, month=5, day=26)).get('good_condition') == 11
        assert calculated_weathers.prepared_data.get(datetime.date(year=2022, month=5, day=27)).get('good_temperature') == 33
        assert calculated_weathers.prepared_data.get(datetime.date(year=2022, month=5, day=27)).get('good_condition') == 11
        assert calculated_weathers.prepared_data.get(datetime.date(year=2022, month=5, day=28)).get('good_temperature') == 34
        assert calculated_weathers.prepared_data.get(datetime.date(year=2022, month=5, day=28)).get('good_condition') == 11


class TestDataAggregationTask:

    def test_run(self, calculated_weathers):
        data_aggregation_task = DataAggregationTask()
        sort_calculated_stats = data_aggregation_task.run(calculated_weathers)

        assert sort_calculated_stats[0][0] == 'PARIS'
        assert sort_calculated_stats[1][0] == 'MOSCOW'

class TestDataAnalyzingTask:

    def test_run(self, sort_calculated_stats, is_csv_file):
        data_analyzing_task = DataAnalyzingTask()
        best_city = data_analyzing_task.run(sort_calculated_stats)

        assert best_city[0] == 'PARIS'


    def test_write_down_data_to_csv_file(self, sort_calculated_stats, is_csv_file):
        data_analyzing_task = DataAnalyzingTask()
        data_analyzing_task.write_down_data_to_csv_file(sort_calculated_stats)

        with open('output.csv', 'r', encoding='utf-8') as csv_file:

            assert is_csv_file == csv_file.read()
