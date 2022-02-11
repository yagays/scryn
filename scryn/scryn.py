import uuid
from typing import List, Dict
from dataclasses import dataclass, field


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


class Scryn:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks
        self.worker2assignment: Dict[Worker, Assignment] = {}
        self.worker2annotation: Dict[Worker, Annotation] = {}

    def get_task(self, worker: Worker) -> Task:
        if worker not in self.worker2annotation:
            # initialize worker's Annotation
            self.worker2annotation[worker] = Annotation(worker_name=worker)
            self.worker2assignment[worker] = Assignment(tasks=self.tasks)

        next_task = next(self.worker2assignment[worker])

        return next_task

    def annotate(self, task: Task, annotation: str, worker: Worker) -> None:
        self.worker2annotation[worker].answers.append(Answer(task_id=task.task_id, answer=annotation))

    def show_annotation(self, worker: Worker) -> None:
        print(self.worker2annotation[worker])
