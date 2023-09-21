# -----
# * aquí se instancia todos los WebDrivers que se necesiten
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


class Drivers:

    def chromeDriver(self):
        # *  Se crea una instancia del Chrome
        return webdriver.Chrome(service=ChromiumService(ChromeDriverManager().install()))

    def edgeDriver(self):
        # *  Se crea una instancia del Microsoft Edge
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

    def firefoxDriver(self):
        # *  Se crea una instancia del FireFox
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))


if __name__ == "__main__":
    pytest.main()
