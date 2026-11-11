import time
import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


@pytest.fixture(scope="function")
def driver():
    # Configure Appium Options for Android
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_id = "48131JEBF16664"
    options.automation_name = "UiAutomator2"

    # Specify the Android Contacts app package and activity
    options.app_package = "com.google.android.contacts"
    options.app_activity = (
        "com.google.android.apps.contacts.activities.PeopleActivity"
    )

    # Connect to the local Appium server
    appium_server_url = "http://127.0.0.1:4723"
    driver = webdriver.Remote(appium_server_url, options=options)

    yield driver

    # Teardown: close session
    driver.quit()


def test_create_contact(driver):
    wait = WebDriverWait(driver, 10)

    # 1. Click Allow button (if permission dialog appears)
    try:
        allow_button = wait.until(
            EC.element_to_be_clickable(
                (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Allow")')
                 )
            )
        allow_button.click()
    except Exception:
        print("Permission dialog did not appear, continuing...")

    # 2. Add wait of 5 seconds
    time.sleep(5)

    # 3. Click on "Create contact" button
    create_contact_btn = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "Create contact")
        )
    )
    create_contact_btn.click()

    # 4. Wait for form to load and enter First Name: "wahed"
    first_name_field = wait.until(
        EC.element_to_be_clickable(
            (AppiumBy.ACCESSIBILITY_ID, "First name")
        )
    )
    first_name_field.send_keys("wahed")

    # 5. Enter Last Name: "MD"
    last_name_field = driver.find_element(
        AppiumBy.ACCESSIBILITY_ID,"Last name"
    )
    last_name_field.send_keys("MD")

    driver.hide_keyboard()
    # # 6. Enter Company field: "XYZ"
    # company_field = driver.find_element(
    #     AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Company")'
    # )
    # company_field.click()
    # time.sleep(2)
    # company_field.clear()
    # time.sleep(3)
    # company_field.send_keys("XYZ")

    # 7. Enter Phone number field: "1234567890"
    phone_field = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone")'
    )
    phone_field.send_keys("1234567890")

    print("\nSuccessfully filled out the contact creation form!")