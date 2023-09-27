import pytest
from tests.testbase import *
from tests.pages.ProductListPage import ProductListPage


class TestRemoveProducts:

    def test_addOneProduct(self, loginSuccessful: tuple[WebDriver, Locators]):
        web, get = loginSuccessful
        productPage = ProductListPage(web, get)

        productPage.addItemToCart(2)
        productPage.gotoShoppingCart()
