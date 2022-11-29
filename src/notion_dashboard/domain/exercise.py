import pandas as pd
from typing import Dict
from datetime import date

from notion_dashboard.dto.notion_property import NotionProperty


class Exercise:
    def __init__(
        self,
        exercise: str,
        date: date,
        repetitions: int,
        sets: float,
        weight: float,
        volume: float,
        type: str,
        **kwargs,
    ):
        self.name = exercise
        self.date = date
        self.repetitions = repetitions
        self.sets = sets
        self.weight = weight
        self.volume = volume
        self.type = type

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    @staticmethod
    def from_json(json_object: Dict) -> "Exercise":
        kwargs = {}
        for name, value_dict in json_object.items():
            notion_property = NotionProperty(name=name, **value_dict)
            kwargs[notion_property.name] = notion_property.value
        return Exercise(**kwargs)


def get_exercise_data_frame(response_body: Dict):
    return pd.DataFrame(
        [Exercise.from_json(x["properties"]).__dict__ for x in response_body["results"]]
    )
