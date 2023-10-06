import requests


url = "https://api.mercadolibre.com/sites/MLA/search?category=MLA1055"


def get_data(url):
    productos = []
    resultados = None
    response = requests.get(url)
    if response.status_code == 200:
        resultados = response.json()
        for resultado in resultados["results"]:
            _resultado = [
                r
                for r in resultado["attributes"]
                if r["name"] == "Marca" and r["value_name"] == "Motorola"
            ]
            if _resultado:
                precio = resultado["price"]
                if precio > 20000 and precio < 80000:
                    productos.append(resultado)

    return productos


resultado = get_data(url)
print(resultado)

"""

¿Que es requests?
Es una libreria que nos permite hacer peticiones a un servidor

¿Que es un endpoint?
Es una URL que nos permite acceder a un recurso
Ej: https://api.mercadolibre.com/users/$USER_ID/items/search?search_type=scan

Metodos:
GET: Obtener datos
POST: Crear datos
PUT: Actualizar datos completa
PATCH: Actualizar datos parcial
HEAD: Obtener encabezados
DELETE: Eliminar datos
OPTIONS: Obtener metodos permitidos

Parametros:
Para hacer filtros de datos category=MLA1055

Si enviamos datos sensibles hay que hacerlo en el header o body.
Man in the middle
https://api.mercadolibre.com/sites/MLA/search?category=MLA1055

curl -X GET -H 'Authorization: Bearer $ACCESS_TOKEN' https://api.mercadolibre.com/users/$USER_ID/items/search?search_type=scan
Usa JWT Json web token

body: encriptado
headers: encriptado
TLS/SSL
certificado digital

"""
# naranjas = ["podrida", "madura", "verde", "podrida", "madura", "verde", "N/S"]

# # Naranja por naranja si la naranja esta podrida la guardamos en la lista. Resultado una lista con todas las naranjas podridas
# podridas = [ojota for ojota in naranjas if ojota == "podrida"]
# maduras = [naranja for naranja in naranjas if naranja == "madura"]
# verdes = [naranja for naranja in naranjas if naranja == "verde"]
# otras = [
#     naranja for naranja in naranjas if naranja not in ["podrida", "madura", "verde"]
# ]
