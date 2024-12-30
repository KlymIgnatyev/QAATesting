import pytest
from modules.api.clients.github import GitHub
from modules.common.database import DataBase
from modules.ui.page_objects.sign_in_page import SignInPage


class User:
    def __init__(self) -> None:
        self.name = None
        self.second_name = None

    def create(self):
        self.name = "Klym"
        self.second_name = "Ignatyev"

    def remove(self):
        self.name = ""
        self.second_name = ""


@pytest.fixture
def user():
    user = User()
    user.create()

    yield user

    user.remove()


@pytest.fixture
def github_api():
    api = GitHub()

    yield api

@pytest.fixture
def database():
    db = DataBase()

    yield db

@pytest.fixture
def sign_in_page():
    sign_in_page = SignInPage()

    yield sign_in_page