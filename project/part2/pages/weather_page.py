from selenium.webdriver.common.by import By
#from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WeatherPage():
    
    # Locators
    SEARCH_FILED = (By.ID, "LocationSearch_input")
    TEMPERATURE_VALUE = (By.CSS_SELECTOR,'[data-testid="TemperatureValue"]')
    US_FROM_DROPDOWN = (By.ID, "LocationSearch_listbox-cb743a230eaef1986f1146684c4f4f244fd4714a889f7452beab62b9dc25e60b")
    
 
    # Methods 
    def __init__(self,driver):
        self.driver = driver
       
    def search_and_select_value(self,value):
        wait = WebDriverWait(self.driver, 10)
        search_box = self.driver.find_element(*self.SEARCH_FILED)
        search_box.click()
        search_box.send_keys(value)
        dropdown_option = wait.until(
          EC.element_to_be_clickable(self.US_FROM_DROPDOWN)
        )
        dropdown_option.click() 
         
    def search(self,value):
        self.driver.find_element(*self.SEARCH_FILED).click()
        self.driver.find_element(*self.SEARCH_FILED).clear()
        self.driver.find_element(*self.SEARCH_FILED).send_keys(value)
        self.driver.find_element(*self.SEARCH_FILED).send_keys(Keys.ENTER)

        
    #get the number temperature (without the °)from the site
    def get_temperature_number(self):
        temp_element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TEMPERATURE_VALUE)
        )
        return float(temp_element.text.replace("°", "").strip())
    
 