import pytest

def test_user_init(first_user, second_user):
    assert first_user.user_name == 'User'
    assert second_user.email == 'John@mail.ru'
    assert len(first_user.task_list) == 4

    assert first_user.user_count == 2
    assert second_user.user_count == 2
    assert first_user.all_tasks_count == 8
    assert second_user.all_tasks_count == 8