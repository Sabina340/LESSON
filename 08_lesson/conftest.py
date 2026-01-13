import pytest
from api_client import ProjectsAPI


@pytest.fixture
def projects_api():
    return ProjectsAPI()


@pytest.fixture
def created_project(projects_api):
    response = projects_api.create_project("Test Project")

    assert response.status_code == 201

    project_id = response.json()["id"]
    return project_id
