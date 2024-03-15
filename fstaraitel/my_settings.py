SECRET_KEY = 'django-insecure-_6w37cs+&d6&@zlm@l^f5t@7kqzbgrw-koq4#2r9)ps=3lmc22'

DATABASES = {
    'default': {
        'ENGINE': 'mssql',
        'NAME': 'db_fstaraitel',
        'HOST': '221.163.82.22',
        'USER': 'sa',
        'PASSWORD': 'Fst23841!',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
            'host_is_server': True,
            'unicode_results': True,
        }
    }
}