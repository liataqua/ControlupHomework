from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class MetricConversionPage():
    
    def __init__(self,driver):
        self.driver = driver
    
    # Locators
    TEMPERATURE_BUTTON  = (By.LINK_TEXT, "Temperature")
    WEIGHT_BUTTON = (By.LINK_TEXT,"Weight")
    LENGTH_BUTTON = (By.LINK_TEXT,"Length")

    # Methods
    def click_button(self,button_name):
        try:
            button_locator = getattr(self, button_name)
            self.driver.find_element(*button_locator).click()
        except AttributeError:
            raise ValueError(f"Locator '{button_name}' does not exist in the class.")