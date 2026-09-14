import pytest
from pydantic import ValidationError

from app.main import PredictionRequest, predict_endpoint, read_root


def test_read_root():
    assert read_root() == {"message": "API is up and running!"}


def test_predict():
    request = PredictionRequest(features=[1.0, 2.0, 3.0])

    assert predict_endpoint(request)["predictions"] == [2.0, 4.0, 6.0]


def test_predict_rejects_invalid_payload():
    with pytest.raises(ValidationError):
        PredictionRequest(features="invalid")
        
def test_predict_incorrect():
    request = PredictionRequest(features=[1.0, 2.0, 3.0])

    assert predict_endpoint(request)["predictions"] != [3.0, 6.0, 9.0]

def test_missing_features():
    invalid_payload = {"wrong_field": [3.5, 1.2, 4.9]}

    with pytest.raises(ValidationError):
        PredictionRequest(**invalid_payload)
