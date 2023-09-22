import pytest
from tests.testbase import *


class TestSuiteLogin:

    # *TC1
    def test_login_success(self, loginSuccessful: tuple[WebDriver, Locators]):
        web, get = loginSuccessful

        items = get.byClasses('inventory_item')
        expect(len(items)).toBeEqual(6)
        wait(2)


if __name__ == "__main__":
    pytest.main()
