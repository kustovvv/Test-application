from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import utils.custom_logger as cl


class Page:
    log = cl.custom_logger()

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator_value, locator_type):
        locator_type = locator_type.lower()
        element = None
        wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])

        if locator_type == "id":
            element = wait.until(lambda x: x.find_element(AppiumBy.ID, locator_value))
            return element
        
        elif locator_type == "class":
            element = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, locator_value))
        
        elif locator_type == "des":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'UiSelector().description("{locator_value}")'))
            
        elif locator_type == "index":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f"UiSelector().index({int(locator_value)})"))
        
        elif locator_type == "text":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, f'text("{locator_value}")'))
        
        elif locator_type == "xpath":
            element = wait.until(
                lambda x: x.find_element(AppiumBy.XPATH, f"{locator_value}"))
            return element
        
        else:
            self.log.info("Locator value " + locator_value + " not found")

        return element

    def find_element(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            self.log.info(
                "Element found with locator_type: " + locator_type + " with the locator_value: " + locator_value)
        except:
            self.log.info(
                "Element not found with locator_type: " + locator_type + " with the locator_value: " + locator_value)

        return element

    def click_element(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.click()
            self.log.info(
                "Clicked on element with locator_type: " + locator_type + " with the locator_value: " + locator_value)
        except:
            self.log.info(
                "Unable to click on element with locator_type: " + locator_type + " with the locator_value: " + locator_value)

        return element

    def send_text(self, text, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.send_keys(text)
            self.log.info(
                "Send text on element with locator_type: " + locator_type + " with the locator_value: " + locator_value)
        except:
            self.log.info(
                "Unable to send text to element with locator_type: " + locator_type + " with the locator_value: " + locator_value)

        return element

    def is_displayed(self, locator_value, locator_type="id"):
        element = None
        try:
            locator_type = locator_type.lower()
            element = self.wait_for_element(locator_value, locator_type)
            element.is_displayed()
            self.log.info(
                "Element with locator_type: " + locator_type + " with the locator_value: " + locator_value + " is displayed")
        except:
            self.log.info(
                "Element with locator_type: " + locator_type + " with the locator_value: " + locator_value + " is not displayed")

        return element

    def key_code(self, value):
        self.driver.press_keycode(value)
