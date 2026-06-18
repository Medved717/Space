from lesson_14_1_9.src.task import Task

class User:
    user_name: str
    email: str
    first_name: str
    last_name: str
    task_list: list
    user_count = 0
    all_tasks_count = 0

    def __init__(self, user_name, email, first_name, last_name, task_list=None):
        self.user_name = user_name
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.task_list = task_list if task_list else []
        User.user_count += 1
        User.all_tasks_count += len(task_list) if task_list else 0

if __name__ == '__main__':
    task = Task('Купить огурцы', 'Покупки для салата.')
    task2 = Task('Купить помидоры', 'Покупки для салата.')
    task3 = Task('Купить сметану', 'Покупки для салата.')
    task4 = Task('Купить соль', 'Покупки для салата.')

    user = User('user', 'user@mail.re', 'user', 'userov', [task, task2, task3, task4])
    print(user.user_name)
    print(user.email)
    print(user.first_name)
    print(user.last_name)
    print(user.task_list)
    print(User.user_count)
    print(user.all_tasks_count)