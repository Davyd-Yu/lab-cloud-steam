from setuptools import setup, find_packages

setup(
    name='my_steam_project',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'mysql-connector-python',
        'azure-identity',
        'azure-keyvault-secrets',
        'flasgger',
        'pyyaml'
    ],
)