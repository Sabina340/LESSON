def test_create_project_positive(projects_api):
    response = projects_api.create_project("New Project")

    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_empty_title(projects_api):
    response = projects_api.create_project("")

    assert response.status_code == 400


def test_get_project_positive(projects_api, created_project):
    response = projects_api.get_project(created_project)

    assert response.status_code == 200
    assert response.json()["id"] == created_project


def test_get_project_negative_wrong_id(projects_api):
    response = projects_api.get_project(99999999)

    assert response.status_code == 404


def test_update_project_positive(projects_api, created_project):
    response = projects_api.update_project(
        created_project, "Updated title"
    )

    assert response.status_code == 200

    get_response = projects_api.get_project(created_project)
    assert get_response.status_code == 200


def test_update_project_negative_wrong_id(projects_api):
    response = projects_api.update_project(99999999, "Name")

    assert response.status_code == 404
