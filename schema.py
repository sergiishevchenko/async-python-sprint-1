from pydantic import BaseModel, BaseSettings


class DetailForecastSchema(BaseModel):
    hour: str
    temp: int
    condition: str


class GeneralForecastSchema(BaseModel):
    date: str
    hours: list[DetailForecastSchema]


class ForecastSchema(BaseModel):
    forecasts: list[GeneralForecastSchema]


class Settings(BaseSettings):

    START_DAY: START_DAY = 9
    END_DAY: END_DAY = 19
    GOOD_CONDITION: GOOD_CONDITION = ('clear', 'partly-cloudy', 'cloudy', 'overcast')
    CSV_FILE: CSV_FILE = 'output.csv'
