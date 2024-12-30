import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_existing(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_exists(github_api):
    repo = github_api.search_repo("become-qa-auto")
    assert repo["total_count"] == 58
    assert "become-qa-auto" in repo["items"][0]["name"]


@pytest.mark.api
def test_repo_not_exists(github_api):
    repo = github_api.search_repo("sergiibutenko_repo_non_exist")
    assert repo["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char(github_api):
    repo = github_api.search_repo("s")
    assert repo["total_count"] != 0
