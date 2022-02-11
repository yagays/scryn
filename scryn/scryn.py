from typing import List, Dict
from dataclasses import dataclass, field

from scryn.task import Task


@dataclass
class Annotation:
    worker_name: str
    annotations: List = field(default_factory=list)


class Scryn:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks
        self.current_task_id = 0
        self.worker2annotation = {}

    def get_task(self, worker: str) -> Task:
        if worker not in self.worker2annotation:
            # initialize worker's Annotation
            self.worker2annotation[worker] = Annotation(worker_name=worker)

        next_task = self.tasks[self.current_task_id]
        self.current_task_id += 1

        return next_task

    def annotate(self, task: Task, annotation: str, worker: str) -> None:
        self.worker2annotation[worker].annotations.append({task.task_id: annotation})

    def show_annotation(self, worker: str) -> None:
        print(self.worker2annotation[worker])
