# Esto es un Comentario.

# * Tipos de Datos Basicos:
a = 1212  # Int
b = 1212.2323  # Float
c = "Hola que onda"  # String
d = True  # Boolean
e = False  # Boolean
f = ["A", 5, True]  # Array
g = (["A", 5, True], ["A", 5, True])  # Tuplas
x = {"key": "123"}  # Objeto


def aprender(framework: str):
    if (framework == 'selenium'):
        return 'Te recomiendo aprender Selenium-Python'
    if (framework == 'cypress'):
        return 'Te recomiendo aprender JavaScript con Promesas'
    if (framework == 'playwright'):
        return 'No hay nada mejor que un TypeScript y un Café'
    return 'No reconozco este framework'


def is_python(framework: str):
    if (framework != 'selenium' or framework == 'playwright'):
        return 'Sí puedes usar Python!'
    else:
        return 'Nop, no se suele usar Python'


def get_all_tests_results(results):
    for result in results:
        while result == 'pass':
            print("TC" + ": " + result)


tests = ["pass", "pass", "pass", "pass", "fail", "fail"]

get_all_tests_results(tests)
