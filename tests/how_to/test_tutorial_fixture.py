import pytest
from tests.drivers.chromedriver import *

#* AHORA! En este Ejemplo vamos a verlo distinto:
# * De qué pasaría si no usamos el Fixture de contexto en el directorio, sino en el mismo archivo así:

class TestFixture:
    #* Definición de la fixture de configuración del navegador
    @pytest.fixture
    def beforeEach(self):
        #* SI vamos a usar el Fixture dentro del mismo Suite (class) se debe crear una nueva instancia del navegador Driver para no tener inconvenientes en los métodos.
        global web, element # Se listan las variables globales del Suite de Prueba.
        web = chromeDriver() # Se retorna una nueva instancia a una variable local.
        element = Locators(web) # Se crea una instancia de Class con todos sus métodos.
        
        element.goto("https://google.com")
        title = web.title
        assert title == "Google"

        yield
        web.quit()
    
    # * Primer caso de prueba
    def test_FirstAutomationTesting(self, beforeEach):
        #* Prueba de automatización: Inserción de texto y clic en el botón de búsqueda
        # Se encuentra el campo de búsqueda y se ingresa el texto "Selenium"
        web.find_element(By.NAME, "q").send_keys("Selenium")
        # Se busca el campo de búsqueda nuevamente y se verifica el texto ingresado
        search_box = web.find_element(By.NAME, "q")
        value = search_box.get_attribute("value")
        assert value == "Selenium"
        
    # * Segundo caso de prueba
    def test_secondTest(self, beforeEach):
        # Prueba adicional
        web.find_element(By.NAME, "q").send_keys("Python")
        # Se busca el campo de búsqueda nuevamente y se verifica el texto ingresado
        search_box = web.find_element(By.NAME, "q")
        value = search_box.get_attribute("value")
        assert value == "Python"
        # Se realiza una aserción simple
    
    
    
if __name__ == "__main__":
    #* Ejecución de las pruebas utilizando pytest
    pytest.main()
