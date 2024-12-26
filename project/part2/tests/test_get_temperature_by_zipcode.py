import pytest
from selenium.webdriver.common.keys import Keys
from part2.pages.weather_page import WeatherPage 
from part2.utils.common import calc_gap_in_precentage
from part2.utils.get_weather import get_current_weather




@pytest.mark.part2
@pytest.mark.usefixtures("driver_part2")
class TestGetTemperatureByZipcode():

    ZIP_CODE = "20852"
    GAP_THRESHOLD = 10  # 10%


    def get_temperature_from_website(self):
        weather_page = WeatherPage(self.driver)
        weather_page.search_and_select_value(self.ZIP_CODE)
        web_temp = weather_page.get_temperature_number()
        return web_temp
      

    def get_temperature_from_api(self):
        api_temp =  get_current_weather(self.ZIP_CODE)
        return api_temp


    def test_check_temperature_gap(self):
        web_temp = self.get_temperature_from_website()
        api_temp = self.get_temperature_from_api()
        print(f"web {web_temp} api {api_temp}")
        gap = calc_gap_in_precentage(web_temp,api_temp)
        assert gap <= self.GAP_THRESHOLD, f"Temperature gap {gap:.2f}% exceeds {self.GAP_THRESHOLD}%."
   
