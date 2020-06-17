from typing import Any, Dict, List, Union

import requests
from requests.exceptions import ConnectionError, HTTPError


def get_person_dob(name: str) -> Union[None, str]:
    try:
        response: requests.models.Response
        with requests.get("https://swapi.dev/api/people/") as response:
            response.raise_for_status()
            resp_dict: Dict[str, Any] = response.json()

        resp_results: List[Dict[str, Any]] = resp_dict["results"]
        resp_person: Dict[str, Any] = next(  # pragma: no cover
            item for item in resp_results if name.lower() in item["name"].lower()
        )
        dob: str = resp_person["birth_year"]
    except HTTPError as http_err:
        raise http_err
    except ConnectionError as ce:
        print(ce)
        raise ce
    except Exception as err:
        print(f"Other error occurred: {err}")
        raise err
    else:
        print(f"successfully retrieved the DOB of {name}")
        return dob
