from pydantic import BaseModel


class DetailForecastSchema(BaseModel):
    hour: str
    temp: int
    condition: str


class GeneralForecastSchema(BaseModel):
    date: str
    hours: list[DetailForecastSchema]


class ForecastSchema(BaseModel):
    forecasts: list[GeneralForecastSchema]
