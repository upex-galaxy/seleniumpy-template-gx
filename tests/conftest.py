import pytest
from tests.drivers.chromedriver import *

@pytest.fixture
def setup():
    web = chromeDriver()
    element = Locators(web)
    element.goto("https://google.com")
    title = web.title
    assert title == "Google"
    
    yield web, element 
    web.quit()
    
    
if __name__ == "__main__":
    pytest.main()
