import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from dotenv import load_dotenv

load_dotenv()



@pytest.fixture(scope="class")
def  init_driver_part1(request):
    driver = webdriver.Chrome()
    driver.get(os.getenv("PART1_URL"))
    driver.maximize_window()
    request.cls.driver = driver
    yield 
    driver.quit()
    

@pytest.fixture(scope="class")
def driver_part2(request):
    service = Service(os.getenv("CHROMEDRIVER_PATH")) 
    driver = webdriver.Chrome(service=service)
    driver.get(os.getenv("PART2_URL"))
    driver.maximize_window()
    request.cls.driver = driver
    yield 
    driver.quit()


