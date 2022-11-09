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
    return pd.DataFrame([Exercise.from_json(x["properties"]).__dict__ for x in response_body["results"]])


if __name__ == "__main__":
    sample = {
        "Date": {
            "id": "%3Cwx%3C",
            "type": "date",
            "date": {"start": "2022-10-20", "end": None, "time_zone": None},
        },
        "Repetitions": {"id": "%3ETGv", "type": "number", "number": 8},
        "Volume": {
            "id": "%5EMOQ",
            "type": "formula",
            "formula": {"type": "number", "number": 1200},
        },
        "Type": {
            "id": "bGEp",
            "type": "multi_select",
            "multi_select": [
                {
                    "id": "05fe4829-6c62-4abf-b64c-76b025c665ab",
                    "name": "Push",
                    "color": "blue",
                }
            ],
        },
        "Weight": {"id": "hYn%7B", "type": "number", "number": 60},
        "Sets": {"id": "%7B%3A%3Et", "type": "number", "number": 2.5},
        "Name": {
            "id": "title",
            "type": "title",
            "title": [
                {
                    "type": "text",
                    "text": {
                        "content": "Incline Press",
                        "link": None
                    },
                    "annotations": {
                        "bold": False,
                        "italic": False,
                        "strikethrough": False,
                        "underline": False,
                        "code": False,
                        "color": "default"
                    },
                    "plain_text": "Incline Press",
                    "href": None
                }
            ]
        },
    }
    print(Exercise.from_json(json_object=sample).__dict__)