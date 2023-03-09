# ESTRUCTURA BASE

# def mi_decorador_con_argumentos(key):
#     def cualquier_nombre(func):
#         def otro_nombre(*args, **kwargs):
#             print('--> antes funcion, argumento:', key)
#             resultado = func(*args, **kwargs)
#             print('--> despues funcion, argumento:', key)
#             return resultado
#         return otro_nombre
#     return cualquier_nombre


# def mi_decorador_sin_argumentos(func):
#     def loremipsum(*args, **kwargs):
#         print('--> antes funcion')
#         resultado = func(*args, **kwargs)
#         print('--> despues funcion')
#         return resultado
#     return loremipsum

# Guia y ejemplos
# https://realpython.com/primer-on-python-decorators/

cache_global = {}

def save_cache(key):
    def dolorsite(func):
        def loremipsum(*args, **kwargs):
            if cache_global.get(key):
                return cache_global.get(key)
            resultado = func(*args, **kwargs)
            cache_global[key] = resultado
            return resultado
        return loremipsum
    return dolorsite


def save_cache_sin_arg(func):
    def loremipsum(*args, **kwargs):
        if cache_global.get("key"):
            return cache_global.get("key")
        resultado = func(*args, **kwargs)
        cache_global["key"] = resultado
        return resultado
    return loremipsum


@save_cache(key="multiplicacion")
def multiplica(param1: int, param2: int) -> int:
    """Multiplica dos parámetros"""
    return param1 * param2


@save_cache(key="suma")
def suma(param1: int, param2: int) -> int:
    """Suma dos parámetros"""
    return param1 + param2


print(multiplica(5, 3))
print(multiplica(10, 4))

print(suma(2,3))
print(suma(10,10))

