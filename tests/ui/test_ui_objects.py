import pytest


@pytest.mark.ui
def test_check_incorrect_username_page_object(sign_in_page):

    # Open GitHub
    sign_in_page.go_to()

    # Try to log in
    sign_in_page.try_login("page_object@gmail.com", "wrongpassword")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    # Close the browser
    sign_in_page.close()
