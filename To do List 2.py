

class Task:
    def __init__(self, name, completed=False):
        self.name = name
        self.completed = completed

    def __str__(self):
        status = "Tamamlandı" if self.completed else "Tamamlanmadı"
        return f"{self.name} - {status}"


class TaskManager:
    def __init__(self, filename="tasks.txt"):
        self.tasks = []
        self.filename = filename
        self.load_tasks()

    def add_task(self, task_name):
        task = Task(task_name)
        self.tasks.append(task)
        print(f"Görev eklendi: {task_name}")

    def complete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].completed = True
            print(f"Görev tamamlandı: {self.tasks[task_index].name}")
        else:
            print("Geçersiz görev indexi!")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Görev silindi: {removed_task.name}")
        else:
            print("Geçersiz görev indexi!")

    def view_tasks(self):
        print("\nTamamlanmamış Görevler:")
        for i, task in enumerate(self.tasks):
            if not task.completed:
                print(f"{i}: {task}")

        print("\nTamamlanmış Görevler:")
        for i, task in enumerate(self.tasks):
            if task.completed:
                print(f"{i}: {task}")

    def save_tasks(self):
        with open(self.filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.name}|{task.completed}\n")
        print("Görevler kaydedildi.")

    def load_tasks(self):
        try:
            with open(self.filename, "r") as file:
                for line in file:
                    name, completed = line.strip().split("|")
                    self.tasks.append(Task(name, completed == "True"))
            print("Görevler yüklendi.")
        except FileNotFoundError:
            print("Görev dosyası bulunamadı. Yeni bir dosya oluşturulacak.")

