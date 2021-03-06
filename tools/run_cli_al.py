from turtle import update

from scryn.scryn import Scryn, Task, Worker
from scryn.strategy import ActiveLearningStrategy


class MLPredictor:
    def predict(self, text):
        # reverse order
        return int(text.split("_")[1])


tasks = [Task(task_id=i, text=f"text_{i}") for i in range(1000)]
worker = Worker(name="yag")

scryn = Scryn(tasks=tasks, strategy=ActiveLearningStrategy(ml_model=MLPredictor(), update_step=3))
num_annotate = 1000

for i in range(num_annotate):
    try:
        task = scryn.get_task(worker)
        if task:
            answer = input(f"{worker.name}:{task.text}: ")
            scryn.annotate(task, answer, worker=worker)
        else:
            break
    except KeyboardInterrupt:
        print()
        break

scryn.show_annotation(worker=worker)
