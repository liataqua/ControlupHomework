import pytest
from part1.pages.category_page import CategoryPage
from part1.pages.metric_conversion_page import MetricConversionPage

@pytest.mark.part1
@pytest.mark.usefixtures("init_driver_part1")
class TestConvertCelsiusToFahrenheit():
    

    def test_celsius_to_fahrenheit(self):
        metric_page = MetricConversionPage(self.driver)     
        metric_page.click_button("TEMPERATURE_BUTTON")
        #remove ad if it's exist (the ad change the URL) 
        if self.driver.current_url != 'https://www.metric-conversions.org/temperature-conversion.htm':
            self.driver.get("https://www.metric-conversions.org/temperature-conversion.htm")
            
        category_page = CategoryPage(self.driver)
        category_page.select_value_from_dropdown("UNIT_FROM_DROPDOWN","Celsius")
        category_page.select_value_from_dropdown("UNIT_TO_DROPDWON","Fahrenheit")
        category_page.enter_value_to_compare("25")
        result_text = category_page.send_result()
        expected_value = "25°C = 77.000°F"
        assert result_text == expected_value, f"Expected '{expected_value}', but got '{result_text}'"
