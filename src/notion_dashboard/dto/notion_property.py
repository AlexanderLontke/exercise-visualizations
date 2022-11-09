from typing import Union
from datetime import date


class NotionProperty:
    def __init__(self, name: str, id: str, type: str, **kwargs):
        self.name = name.lower()
        self.id = id
        self.type = type
        self.value: Union[date, float, str]

        value = kwargs[type]
        if type == "date":
            self.value = date.fromisoformat(value["start"])
        elif type == "number":
            self.value = float(value)
        elif type == "formula":
            self.value = float(value["number"])
        elif type == "multi_select":
            self.value = value[0]["name"]
        elif type == "title":
            self.value = value[0]["plain_text"]
        elif type == "select":
            self.value = value["name"]
        else:
            raise ValueError(f"Type {type} not supported")
