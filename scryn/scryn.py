from typing import List

from scryn.task import Task


class Scryn:
    def __init__(self, tasks: List[Task]) -> None:
        self.tasks = tasks
        self.current_task_id = 0
        self.annotation = {}

    def get_task(self) -> Task:
        next_task = self.tasks[self.current_task_id]
        self.current_task_id += 1

        return next_task

    def annotate(self, task: Task, annotation: str, worker=None) -> None:
        self.annotation[task.task_id] = annotation

    def show_annotation(self, worker=None) -> None:
        print(self.annotation)
