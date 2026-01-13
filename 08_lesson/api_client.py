import requests
from config import BASE_URL, HEADERS


class ProjectsAPI:

    def create_project(self, title):
        return requests.post(
            f"{BASE_URL}/projects",
            headers=HEADERS,
            json={"title": title}
        )

    def get_project(self, project_id):
        return requests.get(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS
        )

    def update_project(self, project_id, title):
        return requests.put(
            f"{BASE_URL}/projects/{project_id}",
            headers=HEADERS,
            json={"title": title}
        )
