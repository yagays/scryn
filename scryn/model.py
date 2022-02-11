import uuid
from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class Worker:
    name: str
    id: uuid.UUID = field(default_factory=uuid.uuid4)


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

    @property
    def num_answers(self):
        return len(self.answers)


class Assignment:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self) -> Optional[Task]:
        if self.i == len(self.tasks):
            return None
        value = self.tasks[self.i]
        self.i += 1
        return value

    def dump_remain_tasks(self):
        return self.tasks[self.i :]
