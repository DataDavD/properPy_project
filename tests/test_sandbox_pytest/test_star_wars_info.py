from unittest.mock import patch

import pytest

from sandbox_pytest.star_wars_info import get_person_dob, requests


@pytest.mark.parametrize(
    "arg_names, add_exp_result", [("Luke Skywalker", "19BBY"), ("Darth Vader", "41.9BBY")]
)
def test_get_dob(arg_names, add_exp_result) -> None:
    assert get_person_dob(arg_names) == add_exp_result


@patch.object(
    requests,
    "get",
    side_effect=[requests.exceptions.HTTPError, requests.exceptions.ConnectionError, Exception],
)
def test_dob_erros(mock_requests) -> None:
    with pytest.raises(requests.exceptions.HTTPError):
        get_person_dob("Darth Vader")
    with pytest.raises(requests.exceptions.ConnectionError):
        get_person_dob("Darth Vader")
    with pytest.raises(Exception):
        get_person_dob("Darth Vader")


def test_mock_dob() -> None:
    with patch.object(requests, "get") as mock_response:
        mock_response.return_value.__enter__.return_value.json.return_value = {
            "results": [
                {"name": "Luke Skywalker", "birth_year": "19BBY"},
                {"name": "Darth Vader", "birth_year": "41.9BBY"},
            ]
        }
        assert get_person_dob("Luke Skywalker") == "19BBY"
        mock_response.assert_called_once()
        assert get_person_dob("Darth Vader") == "41.9BBY"
        mock_response.assert_called()
