import json

import pytest
from src.models.history_model import HistoryModel


# Req. 7
@pytest.mark.usefixtures("prepare_base")
def test_request_history():
    json_data = HistoryModel.list_as_json()
    data = json.loads(json_data)

    assert data  # Verifica se a lista não está vazia
    assert len(data) == 2  # Verifica se a lista tem 2 elementos
    assert data[0]["text_to_translate"] == "Hello, I like videogame"
    assert data[1]["text_to_translate"] == "Do you love music?"
    assert data[0]["translate_from"] == "en"
    assert data[1]["translate_from"] == "en"
