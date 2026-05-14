import json
import pandas as pd
import pytest
from ls_13_1_3.task_1 import titanic_sort_table



def test_titanic_sort_table(titanic_df):
    expected_result = {'Мужчины': 28.5, 'Женщины': 33.0}
    assert titanic_sort_table(titanic_df) == json.dumps(expected_result)


