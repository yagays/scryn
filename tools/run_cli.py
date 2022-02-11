from scryn.scryn import Scryn
from scryn.task import Task

tasks = [Task(task_id=i, text=f"text_{i}") for i in range(1000)]
task_category = "TextClassification"
strategy = "random"
worker = "yag"

scryn = Scryn(tasks=tasks)
num_annotate = 1000

for i in range(num_annotate):
    task = scryn.get_task(worker)
    try:
        answer = input(task.text + ": ")
        scryn.annotate(task, answer, worker=worker)
        print(answer)
    except KeyboardInterrupt:
        break

print()
scryn.show_annotation(worker=worker)
