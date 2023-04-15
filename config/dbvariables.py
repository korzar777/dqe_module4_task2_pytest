
#default database configuration - should be used in config file or db, may be encripted
def db_variables(key=None):
    variables = {'server':  'db',  #'localhost',
                 'port': '3306', # '1433', #'57175',
                 'database': 'TRN',
                 'username': 'DQTestUser',
                 'password': 'DQTesting111'
                }
    return variables if key is None else None if key not in variables else variables[key]