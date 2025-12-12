import mysql.connector
import yaml
import os
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

# Знаходимо шлях до конфігу
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG_PATH = os.path.join(BASE_DIR, 'config', 'app.yml')


def get_db_connection():
    with open(CONFIG_PATH, "r") as f:
        config = yaml.safe_load(f)

    try:
        # Спроба підключитися через Azure Key Vault
        credential = DefaultAzureCredential()
        client = SecretClient(vault_url=config['key_vault_url'], credential=credential)

        db_user = client.get_secret(config['secret_names']['user']).value
        db_password = client.get_secret(config['secret_names']['password']).value
        db_host = client.get_secret(config['secret_names']['host']).value
    except Exception as e:
        print(f"Warning: Azure Key Vault not found. Error: {e}")
        # Якщо хочеш тестити локально без Key Vault - розкоментуй рядок нижче і впиши свої дані:
        # return mysql.connector.connect(user='root', password='password', host='localhost', database='steam_db')
        raise e

    return mysql.connector.connect(
        user=db_user,
        password=db_password,
        host=db_host,
        database='steam_db',
        ssl_disabled=True
    )