import pytest
from tests.drivers.chromedriver import *

#* Este es otro ejemplo de Suite usando otro Fixture y con más de un caso de Prueba:

class TestSuite:
    
    @pytest.fixture
    def precondition(self):
        global web, element
        web = chromeDriver()
        element = Locators(web)
        
        element.goto("https://www.selenium.dev/selenium/web/web-form.html")
        title = web.title
        assert title == "Web form"
        
        yield
        web.quit()
    
    def test_TC1_FirstExample(self, precondition):

        textBox = element.getSelector("[name='my-text']")
        submitButton = element.getSelector("[type='submit']")
        textBox.send_keys("Selenium")
        submitButton.click()
        message = element.getID("message")
        value = message.text
        assert value == "Received!"

        
    def test_TC2_SecondExample(self):

        textBox = element.getSelector("[name='my-text']")
        submitButton = element.getSelector("[type='submit']")
        textBox.send_keys("UPEX")
        submitButton.click()
        message = element.getID("message")
        value = message.text
        assert value == "Received!"
                
        
if __name__=='__main__':
    pytest.main()