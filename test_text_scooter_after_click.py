import time
from selenium import webdriver
from urban_routes_main_page import UrbanRoutesPage  # Import the POM class

def test_custom_scooter_option():
    # Step 1: Open the app - update the URL after starting the server
    driver = webdriver.Chrome()
    driver.get('https://cnt-a56ab7f9-a8e6-424a-afe7-75f8f2ae1364.containerhub.tripleten-services.com/')

    # Create an instance of the page class
    urban_routes_page = UrbanRoutesPage(driver)

    # Step 3: Use POM methods to perform actions on the page
    # Enter "From" and "To" locations.
    # Use the "enter_locations" step to enter both locations
    urban_routes_page.enter_locations('East 2nd Street, 601', '1300 1st St')

    # Select the "Custom" option.
    urban_routes_page.click_custom_option()
    time.sleep(2)  # Adding delay for visibility; optional

    # Click the "Scooter" icon.
    urban_routes_page.click_scooter_icon()
    time.sleep(2)  # Adding delay for visibility; optional

    actual_value = urban_routes_page.get_duration_text()
    expected_value = "Duration"
    assert expected_value in actual_value, f"Expected '{expected_value}', but got '{actual_value}'"

    driver.quit()