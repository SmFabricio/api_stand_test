import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH)

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_users_table()
print(response.status_code)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)

response = post_new_user(data.user_body);
print(response.status_code)
print(response.json()) # Para mostrar la autorización Token para crear usuario

def post_products_kits(products_ids):
    # Realiza una solicitud POST para buscar kits por productos.
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, # Concatenación de URL base y ruta.
                         json=products_ids, # Datos a enviar en la solicitud.
                         headers=data.headers) # Encabezados de solicitud.


response = post_products_kits(data.product_ids);
""" print(response.status_code)
print(response.json()) # Muestra del resultado en la consola """



