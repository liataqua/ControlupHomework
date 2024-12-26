import pytest
from part1.pages.category_page import CategoryPage
from part1.pages.metric_conversion_page import MetricConversionPage


@pytest.mark.part1
@pytest.mark.usefixtures("init_driver_part1")
class TestConvertmetersTofeet():
    
    def test_meters_to_feet(self):
        metric_page = MetricConversionPage(self.driver)     
        metric_page.click_button("LENGTH_BUTTON")        
        #remove ad if it's exist (the ad change the URL) 
        if self.driver.current_url != 'https://www.metric-conversions.org/length-conversion.htm':
            self.driver.get("https://www.metric-conversions.org/length-conversion.htm")
            
        category_page = CategoryPage(self.driver)
        category_page.select_value_from_dropdown("UNIT_FROM_DROPDOWN","Meters")
        category_page.select_value_from_dropdown("UNIT_TO_DROPDWON","Feet")
        category_page.enter_value_to_compare("900")
        result_text = category_page.send_result()
        expected_value = "900m = 2952.8ft"
        assert result_text == expected_value, f"Expected '{expected_value}', but got '{result_text}'"