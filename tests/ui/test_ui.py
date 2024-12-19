import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time


@pytest.mark.ui
def test_check_incorrect_username():
    #Controlling the browser
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install())
    )


    #Open GitHub
    driver.get("https://github.com/login")


    #Search for the name/email field
    login_elem = driver.find_element(By.ID, "login_field")

    #Search for the password field
    pass_elem = driver.find_element(By.ID, "password")

    #Insert incorrect information
    login_elem.send_keys("wronginformation@email.com")
    pass_elem.send_keys("12345")


    #Press "Sign in"
    btn_elem = driver.find_element(By.NAME, "commit")
    btn_elem.click()

    #CHeck the page title
    assert driver.title == "Sign in to GitHub · GitHub"

    #closing the browser
    driver.close()