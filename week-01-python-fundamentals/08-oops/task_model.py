class Task:
    def __init__(self, id, title, description):
        #Validation Check.
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        
        #If valid, save the data.
        self.id = id
        self.title = title
        self.description = description
        self.status = "TODO"
    
    def mark_as_done(self):
        self.status = "DONE"

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

class TaskNotFoundError(Exception):
    pass

try:
     raise TaskNotFoundError(f"Task (ID: {{id}}) was not found in the database!")
except TaskNotFoundError as e:
    print("Custom Error Handled", e)


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description):
        new_task = Task(self.next_id, title, description)
        self.tasks.append(new_task)
        self.next_id += 1
        return new_task

    def get_task(self, task_id):
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise TaskNotFoundError(f"Task (ID: {task_id}) was not found in the database!")

    def delete_task(self, task_id):
        task=self.get_task(task_id)
        self.tasks.remove(task)
        print(f"Task (ID: {task_id}) deleted successfully!")
        return task
        
    def filter_by_status(self, status):
        return[task for task in self.tasks if task.status == status.upper()]

# task_1 = Task(1, "Buy groceries", "Buy groceries from the supermarket")
# print("Before:", task_1.to_dict())

# task_1.mark_as_done()
# print("After:", task_1.to_dict())

# task_2 = Task(2, "Learn Python", "Testing valid title")
# print("Valid Task Created:", task_2.title)

# try:
#     task_3 = Task(3, " ", "Invalid Task")
#     print("Task Created:", task_3.title) # This line won't execute
# except ValueError as e:
#     print("Error:", e)

manager = TaskManager()

t1 = manager.add_task("Learn OOP", "Understand classes and objects")
t1.mark_as_done()
t2 = manager.add_task("Build task manager", "Pure python cli project")

print(f"Total tasks created: {len(manager.tasks)}")

found=manager.get_task(2)
print("Found task:",found.title)

try:
    manager.get_task(99)
except TaskNotFoundError as e:
    print(f"Handling missing task: {e}")

done_tasks = manager.filter_by_status("DONE")
print(f"Tasks marked as DONE: {[t.title for t in done_tasks]}")

deleted = manager.delete_task(1)
print(f"Deleted task: {deleted.title}")
print(f"Total tasks remaining: {len(manager.tasks)}")