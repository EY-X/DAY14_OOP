class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        
        
    def __repr__(self):
        return f'The description: {self.description} The due date: {self.due_date}'

class TodoList:
    def __init__(self, description, due_date):
        self.tasks = []
    

    def add_task(self, description, due_date):
        self.tasks.append(Task(self.description, self.due_date))






eden = Task('travel', 'december')
print(eden)
jay = Task('shopping', 'every sunday')
print(jay)
chiam = Task('workout', 'every-day')
print(chiam)

# final_to_do_list = TodoList()

# to_do.add_task('work', 'weekdays')
# to_do.add_task('chill', 'never')
# to_do.add_task('coding', 'everyday')







