import uuid
from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True)
class Worker:
    name: str
    id: str = field(default_factory=uuid.uuid4)


@dataclass
class Task:
    task_id: str
    text: str


@dataclass
class Answer:
    task_id: str
    answer: str


@dataclass
class Annotation:
    worker_name: str
    answers: List[Answer] = field(default_factory=list)


class Assignment:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i == len(self.tasks):
            raise StopIteration()
        value = self.tasks[self.i]
        self.i += 1
        return value
