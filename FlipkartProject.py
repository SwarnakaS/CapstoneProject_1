import pytest
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


#Initialize the WebDriver
@pytest.fixture
def driver():
    driver = webdriver.Chrome(executable_path="C:\\Users\\SISPAMPATHY\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver.maximize_window()
    yield driver

#Step 01: Open Flikart E-commerce Application
driver.get("https://www.flipkart.com/")
assert "Flipkart" in driver.title
assert driver.find_element(By.XPATH,"//img[@alt='Flipkart']")

#Step 02: Search for "Macbook air m2"
search_box = driver.find_element_by_name("q")
search_box.clear()
search_box.send_keys("Macbook air m2")
search_box.send_keys(Keys.RETURN)

#Step 03: Click on the first displayed Item
first_item = driver.find_element(By.CSS_SELECTOR,"div._396cs4")
first_item.click()

#Step 04: Click on the "Add To Cart" button
add_to_cart_button = driver.find_element(By.CSS_SELECTOR,"button._2KpZ6l _2U9uOA _3v1-ww")
add_to_cart_button.click()

#Step 05: Verify that the item has been added to the cart successfully
assert "Item added to cart" in driver.get_page_source()

#Close the browser window
driver.quit()

#Run the test with pytest
if __name__ == "__main__":
    pytest.main()
