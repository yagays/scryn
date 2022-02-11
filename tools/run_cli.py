from scryn.scryn import Scryn, Task, Worker

tasks = [Task(task_id=i, text=f"text_{i}") for i in range(1000)]
task_category = "TextClassification"
strategy = "random"
worker = Worker(name="yag")

scryn = Scryn(tasks=tasks)
num_annotate = 1000

for i in range(num_annotate):
    task = scryn.get_task(worker)
    try:
        answer = input(f"{worker.name}:{task.text}: ")
        scryn.annotate(task, answer, worker=worker)
    except KeyboardInterrupt:
        print()
        break

worker2 = Worker(name="ays")
for i in range(num_annotate):
    task = scryn.get_task(worker2)
    try:
        answer = input(f"{worker2.name}:{task.text}: ")
        scryn.annotate(task, answer, worker=worker2)
    except KeyboardInterrupt:
        print()
        break

print()
scryn.show_annotation(worker=worker)
scryn.show_annotation(worker=worker2)
