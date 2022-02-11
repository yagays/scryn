import pytest

from scryn.model import Task, Worker
from scryn.scryn import Scryn


@pytest.fixture(scope="module")
def dummy_tasks():
    return [Task(task_id=i, text=f"text_{i}") for i in range(100)]


@pytest.fixture(scope="module")
def w1():
    return Worker(name="w1")


@pytest.fixture(scope="module")
def w2():
    return Worker(name="w1")


def test_get_tasks(dummy_tasks, w1):
    scryn = Scryn(tasks=dummy_tasks)

    assert scryn.get_task(worker=w1) == Task(task_id=0, text="text_0")


def test_get_tasks_multiple_workers(dummy_tasks, w1, w2):
    scryn = Scryn(tasks=dummy_tasks)

    # worker 1
    assert scryn.get_task(worker=w1) == Task(task_id=0, text="text_0")
    assert scryn.get_task(worker=w1) == Task(task_id=1, text="text_1")
    # worker 2
    assert scryn.get_task(worker=w2) == Task(task_id=0, text="text_0")
    # then, worker 1
    assert scryn.get_task(worker=w1) == Task(task_id=2, text="text_2")


def test_annotate(dummy_tasks, w1):
    scryn = Scryn(tasks=dummy_tasks)
    task = scryn.get_task(worker=w1)

    # before annotaiton
    assert len(scryn.worker2annotation[w1].answers) == 0

    scryn.annotate(annotation="annotated", task=task, worker=w1)
    # after annotation
    assert scryn.worker2annotation[w1].worker_name == w1.name
    assert len(scryn.worker2annotation[w1].answers) == 1
    assert scryn.worker2annotation[w1].answers[0].task_id == 0
    assert scryn.worker2annotation[w1].answers[0].answer == "annotated"
