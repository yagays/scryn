from typing import Dict, List, Set

from scryn.model import Annotation, Answer, Assignment, Task, Worker
from scryn.strategy import BaseStrategy, VanillaStrategy


class Scryn:
    def __init__(self, tasks: List[Task], strategy: BaseStrategy = VanillaStrategy()) -> None:
        self.tasks = tasks
        self.strategy = strategy
        self.workers: Set[Worker] = set()

        self.worker2assignment: Dict[Worker, Assignment] = {}
        self.worker2annotation: Dict[Worker, Annotation] = {}

    def get_task(self, worker: Worker) -> Task:
        if worker not in self.workers:
            self._initialize_worker(worker)

        next_task = next(self.worker2assignment[worker])

        return next_task

    def annotate(self, task: Task, annotation: str, worker: Worker) -> None:
        self.worker2annotation[worker].answers.append(Answer(task_id=task.task_id, answer=annotation))

    def show_annotation(self, worker: Worker) -> None:
        print(self.worker2annotation[worker])

    def _initialize_worker(self, worker: Worker):
        self.workers.add(worker)

        # initialize worker's Annotation
        self.worker2annotation[worker] = Annotation(worker_name=worker)

        # initialize and ranking Assignment's tasks
        assign_task = self.strategy.ranking(self.tasks)
        self.worker2assignment[worker] = Assignment(tasks=assign_task)
