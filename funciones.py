


def mi_funcion_pura_multiplicacion(param1:int, param2:int) -> int:
    return (param1 * param2)

def mi_funcion_pura_suma(param1:int, param2:int) -> int:
    return (param1 + param2)

def mi_funcion_superior(func, param1, param2):
    return func(param1, param2)


result = mi_funcion_superior(mi_funcion_pura_suma, 10, 100)
print(result)

