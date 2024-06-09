from workflow import show_info
from prefect import flow
from prefect.testing.utilities import prefect_test_harness
import pytest
import httpx


@pytest.fixture(autouse=True, scope="session")
def prefect_test_fixture():
    with prefect_test_harness():
        yield


def test_workflow_without_time(mocker):
    mocker_response = mocker.Mock()
    mocker_response.json.return_value = {
        "info": {"count": 20},
        "results": [{"name": "Rick Test"}],
    }
    mocker.patch("httpx.get", return_value=mocker_response)
    mocker.patch("random.choice", return_value=1)
    workflow = show_info("Rick")
    assert workflow[0].type.value == "COMPLETED"
