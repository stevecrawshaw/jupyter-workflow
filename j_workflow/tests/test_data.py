import pandas as pd
from j_workflow.data import get_fremont_data

def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ["Total", "West", "East"])
    assert isinstance(data.index, pd.DatetimeIndex)
    

