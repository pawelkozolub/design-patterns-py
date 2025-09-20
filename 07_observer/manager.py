from observer import Observer

class Manager(Observer):

    def notify(self, *args, **kwargs):
        worker = kwargs["worker"]
        progress = args[0]
        
        if progress > 70:
            print(f"I need to search new task for Worker {worker}.")
        else:
            print(f"Worker {worker} still works on current task, reported progress is {progress}.")