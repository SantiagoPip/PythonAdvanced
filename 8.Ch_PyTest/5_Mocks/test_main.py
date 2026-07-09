from main import api_call
import pytest
def test_api_call(mocker):
    mock_get  = mocker.patch("main.requests.get")