import pytest
from tests.testbase import *


class TestSuiteLogin:

    # *TC1
    def test_login_success(self, beforeEach: Test):
        web, get = beforeEach
        get.byDataTest('username').send_keys('standard_user')
        get.byDataTest('password').send_keys('secret_sauce')
        wait(1)
        get.byDataTest('login-button').click()
        expect(web.current_url).toContain("/inventory")


if __name__ == "__main__":
    pytest.main()
