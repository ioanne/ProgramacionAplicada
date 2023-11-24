from folder1.file1 import FileOne, FileTwo

print(FileOne)
print(FileTwo)


"""
    Módulo:
    Un módulo es un archivo que contiene definiciones y declaraciones de Python.
    Estos archivos tienen la extensión .py y pueden contener variables, funciones, clases y otros componentes de Python.
    Los módulos se utilizan para organizar el código en archivos separados para facilitar la reutilización y la gestión.

    Un módulo en Python puede ser:
    Un archivo individual que contiene código Python y puede ser importado y utilizado en otros programas.
    Una colección de funciones, clases o variables: Puede agrupar múltiples funciones,
    clases o variables relacionadas en un solo archivo para facilitar su acceso y reutilización.


    Paquete:
    Un paquete es una estructura que permite organizar módulos relacionados en subdirectorios
    para facilitar la modularidad y la reutilización de código.
    Los paquetes son colecciones de módulos que están organizados jerárquicamente en un sistema de directorios.

    Un paquete puede contener uno o varios archivos de módulos (archivos .py)
    y también puede incluir subpaquetes (otros directorios que contienen módulos y posiblemente otros subpaquetes).
    
    Requiere un archivo especial __init__.py
    Para que Python reconozca un directorio como un paquete, debe contener un archivo llamado __init__.py.
    Este archivo puede estar vacío o puede contener código de inicialización para el paquete.





    Los imports relativos en Python se usan para importar módulos dentro del mismo paquete, utilizando una notación especial.
    Sin embargo, hay algunas consideraciones importantes que debes tener en cuenta al trabajar con imports relativos:

    Ubicación del script de ejecución:
    Los imports relativos funcionan mejor cuando se utilizan dentro de un paquete, y el script principal se ejecuta desde ese paquete.
    Esto significa que el script que se ejecuta debe estar dentro de la jerarquía del paquete para que los imports relativos funcionen correctamente.
    
    
    Notación para imports relativos:
    La notación para los imports relativos comienza con uno o más puntos (.)
    para indicar la ubicación relativa del módulo que estás importando en relación con el módulo actual.
    Un solo punto (.) se refiere al módulo actual, dos puntos (..) se refieren al directorio padre y así sucesivamente.

"""
