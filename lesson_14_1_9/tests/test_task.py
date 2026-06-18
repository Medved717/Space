import pytest
from lesson_14_1_9.src.task import Task
from lesson_14_1_9.src.user import User


def test_task_init(task):
    assert task.name == 'Покупка огурцов'
    assert task.description == 'Необходимо сходить в магазин и совершить покупку огурцов.'
    assert task.status == 'Ожидает старта'
    assert task.created_at == '17.06.2026'