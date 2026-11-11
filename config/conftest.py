import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options


@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_id = "48131JEBF16664"
    options.automation_name = "UiAutomator2"

    # Specify the Android Contacts app package and activity
    options.app_package = "com.google.android.contacts"
    options.app_activity = (
        "com.google.android.apps.contacts.activities.PeopleActivity")
    options.no_reset = True

    # Connect to local Appium server
    appium_server_url = "http://127.0.0.1:4723"

    driver = webdriver.Remote(appium_server_url, options=options)
    driver.implicitly_wait(10)

    yield driver

    # Teardown
    driver.quit()



