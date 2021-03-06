import random
from abc import ABC, abstractmethod
from typing import List

from scryn.model import Task


class BaseStrategy(ABC):
    def __init__(self, update_step: int = -1) -> None:
        self.update_step = update_step

    @abstractmethod
    def ranking(self, tasks: List[Task]) -> List[Task]:
        pass


class VanillaStrategy(BaseStrategy):
    def ranking(self, tasks: List[Task]) -> List[Task]:
        return tasks


class RandomOrderStrategy(BaseStrategy):
    def ranking(self, tasks: List[Task]) -> List[Task]:
        random.shuffle(tasks)
        return tasks


class ActiveLearningStrategy(BaseStrategy):
    def __init__(self, ml_model, update_step: int) -> None:
        self.ml_model = ml_model
        self.update_step = update_step

    def ranking(self, tasks: List[Task]) -> List[Task]:
        tasks_with_confidence = [(t, self.ml_model.predict(t.text)) for t in tasks]
        sorted_tasks = sorted(tasks_with_confidence, key=lambda x: x[1], reverse=True)

        return [t[0] for t in sorted_tasks]
