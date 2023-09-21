import pytest
# * 🧪 ESTE es un archivo que puede englobar TODAS las interacciones con las pruebas, sobretodo la instancia del driver.
from selenium.webdriver.remote.webdriver import WebDriver
from tests.utils.drivers import Drivers
from tests.utils.locators import Locators


# * Modules:
Drivers
Locators

# * Interface:
WebDriver
Test = tuple[WebDriver, Locators]


if __name__ == "__main__":
    pytest.main()
