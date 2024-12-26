from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class CategoryPage():
    
    def __init__(self,driver):
        self.driver = driver
        
    #Locators
    CELSIUS_BUTTON = (By.LINK_TEXT, "Celsius")
    UNIT_TO_DROPDWON = (By.ID,"unitTo")
    UNIT_FROM_DROPDOWN = (By.ID, "unitFrom")
    VALUE_TO_COMPARE_INPUT = (By.ID, "arg")
    RESULT_TEXT = (By.ID,"answerDisplay")

    # Methods
    def select_value_from_dropdown(self,dropdown,value):
        try:
          dropdown_locator = getattr(self, dropdown)
          select = Select(self.driver.find_element(*dropdown_locator))
          select.select_by_visible_text(value)
        except AttributeError:
            raise ValueError(f"Locator '{dropdown}' does not exist in the class.")

    def enter_value_to_compare(self,value):
        self.driver.find_element(*self.VALUE_TO_COMPARE_INPUT).click()
        self.driver.find_element(*self.VALUE_TO_COMPARE_INPUT).clear()
        self.driver.find_element(*self.VALUE_TO_COMPARE_INPUT).send_keys(value)

    def send_result(self):
        text = self.driver.find_element(*self.RESULT_TEXT).text
        return text
        
        


