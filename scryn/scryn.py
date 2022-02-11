from typing import Dict, List, Optional, Set

from scryn.model import Annotation, Answer, Assignment, Task, Worker
from scryn.strategy import BaseStrategy, VanillaStrategy


class Scryn:
    def __init__(self, tasks: List[Task], strategy: BaseStrategy = VanillaStrategy()) -> None:
        self.tasks = tasks
        self.strategy = strategy
        self.workers: Set[Worker] = set()

        self.worker2assignment: Dict[Worker, Assignment] = {}
        self.worker2annotation: Dict[Worker, Annotation] = {}

    def get_task(self, worker: Worker) -> Optional[Task]:
        if worker not in self.workers:
            self._initialize_worker(worker)

        next_task = next(self.worker2assignment[worker])

        # update step
        if next_task and self._is_update_step(worker):
            self._update_assignment(worker)

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

    def _is_update_step(self, worker):
        if self.strategy.update_step == -1:
            return False

        current_steps = self.worker2annotation[worker].num_answers
        if current_steps % self.strategy.update_step == 0:
            return True
        else:
            return False

    def _update_assignment(self, worker):
        remain_tasks = self.worker2assignment[worker].dump_remain_tasks()
        assign_task = self.strategy.ranking(remain_tasks)
        print(len(remain_tasks))
        self.worker2assignment[worker] = Assignment(tasks=assign_task)
