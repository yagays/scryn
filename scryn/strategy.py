import random
from abc import ABC, abstractmethod
from typing import List

from scryn.model import Task


class BaseStrategy(ABC):
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
