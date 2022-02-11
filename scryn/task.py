from dataclasses import dataclass


@dataclass
class Task:
    task_id: str
    text: str


@dataclass
class TextTask:
    pass


@dataclass
class TextClassificationTask:
    pass


@dataclass
class ImageTask:
    pass
