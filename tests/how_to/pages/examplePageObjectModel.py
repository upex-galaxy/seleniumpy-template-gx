from tests.drivers.chromedriver import *
from selenium.webdriver.remote.webdriver import WebDriver
from tests.drivers.chromedriver import Locators

class ExampleLoginPage:
    def __init__(self, driver: WebDriver, locators: Locators):    
        self.web = driver    
        self.element = locators
        # todo: Elements:
        self.usernameInput = ('[data-test="username"]')
        self.passwordInput = ('[data-test="password"]')
        self.loginButton = ('[data-test="login-button"')

    def getLoginUserValue(self):
        return self.element.getID('login_credentials').text.split("\n")[1]
    
    def getLoginPasswordValue(self):
        return self.element.getClass('login_password').text.split("\n")[1]
        
    def enterUsername(self, username):
        self.element.getSelector(self.usernameInput).send_keys(username)
        
    def enterPassword(self, password):
        self.element.getSelector(self.passwordInput).send_keys(password)
    
    def submitLogin(self):
        self.element.getSelector(self.loginButton).click()
        
    
if __name__ == "__main__":
    pass