import sys


# sql query samples
def query_samples(key=None):
    variables = {
        'TABLE_CHECKS_SQL_GROUP1': 'SELECT {} FROM {}.{} group by {} having {}',
        'TABLE_CHECKS_SQL_SELECT0': 'SELECT {} FROM {}.{}',
        'TABLE_CHECKS_SQL_SELECT1': 'SELECT {} FROM {}.{} where {}'
    }
    return variables if key is None else None if key not in variables else variables[key]


# db, tables
def db_tables(key=None):
    variables = {
        # 'TRN_DB':'TRN',
        'TRN_TABLE_EMPLOYEES': 'hr.employees',
        'TRN_TABLE_JOBS': 'hr.jobs',
        'TRN_TABLE_LOCATIONS': 'hr.locations'
    }
    return variables if key is None else None if key not in variables else variables[key]


def jobid_jobtitle_pairs():
    variables = {1: 'Public Accountant',
                 2: 'Accounting Manager',
                 3: 'Administration Assistant',
                 4: 'President',
                 5: 'Administration Vice President',
                 6: 'Accountant',
                 7: 'Finance Manager',
                 8: 'Human Resources Representative',
                 9: 'Programmer',
                 10: 'Marketing Manager',
                 11: 'Marketing Representative',
                 12: 'Public Relations Representative',
                 13: 'Purchasing Clerk',
                 14: 'Purchasing Manager',
                 15: 'Sales Manager',
                 16: 'Sales Representative',
                 17: 'Shipping Clerk',
                 18: 'Stock Clerk',
                 19: 'Stock Manager'
                 }
    return variables
