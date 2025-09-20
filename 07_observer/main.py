from worker import Worker
from manager import Manager

worker = Worker("Adam")
manager1 = Manager(worker)
manager2 = Manager(worker)

for _ in range(20):
    worker.do_work()