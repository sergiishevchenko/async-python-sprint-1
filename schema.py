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

    START_DAY: int = 9
    END_DAY: int = 19
    GOOD_CONDITION: tuple = ('clear', 'partly-cloudy', 'cloudy', 'overcast')
    CSV_FILE: str = 'output.csv'
