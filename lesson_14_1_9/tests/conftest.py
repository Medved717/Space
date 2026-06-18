import pytest
from lesson_14_1_9.src.task import Task
from lesson_14_1_9.src.user import User

@pytest.fixture
def first_user():
    return User(
        user_name='User',
        email='user@mail.ru',
        first_name='User',
        last_name='Userov',
        task_list=[
            Task('Покупка огурцов', 'Необходимо сходить в магазин и совершить покупку огурцов.'),
            Task('Покупка помидоров', 'Необходимо сходить в магазин и совершить покупку помидоры.'),
            Task('Покупка соли', 'Необходимо сходить в магазин и совершить покупку соли.'),
            Task('Покупка сметаны', 'Необходимо сходить в магазин и совершить покупку сметаны.')
    ]
    )

@pytest.fixture
def second_user():
    return User(
        user_name='John',
        email='John@mail.ru',
        first_name='John',
        last_name='Johnov',
        task_list=[
            Task('Покупка огурцов', 'Необходимо сходить в магазин и совершить покупку огурцов.'),
            Task('Покупка помидоров', 'Необходимо сходить в магазин и совершить покупку помидоры.'),
            Task('Покупка соли', 'Необходимо сходить в магазин и совершить покупку соли.'),
            Task('Покупка сметаны', 'Необходимо сходить в магазин и совершить покупку сметаны.')
    ]
    )

@pytest.fixture()
def task():
    return Task('Покупка огурцов', 'Необходимо сходить в магазин и совершить покупку огурцов.',
                created_at='17.06.2026')
