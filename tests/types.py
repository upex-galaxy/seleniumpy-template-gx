from selenium.webdriver.remote.webdriver import WebDriver
from tests.drivers.chromedriver import Locators

test = tuple[WebDriver, Locators]

if __name__ == "__main__":
    print("Test Types File open")