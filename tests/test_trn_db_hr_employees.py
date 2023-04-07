import pytest
import allure
from libs.helpers.libs import Helpers
from libs.helpers.dbLib import DbLib
from config.variables import *
from config.dbvariables import *
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.employees
@pytest.mark.tc1
@pytest.mark.parametrize("querysample, tabletouse, expvalue",
                         [('TABLE_CHECKS_SQL_GROUP1', 'TRN_TABLE_EMPLOYEES', 0)
                          ])
def test_employees_has_no_duplicates(querysample, tabletouse, expvalue):
    '''Case verifies that no duplicate rows exist in hr.employees table
    *Test Steps:*
    1. Execute prepared query and migrate to pandas DataFrame
    2. Check number of rows returned is correct
    *Expected result:*
    1. Number of records returned by query is 0
    2. Each returned records (Failed) must be logged
    '''
    allure.dynamic.title(f'Verified that {tabletouse} '
                         f'has no duplicates')
    test_query = Helpers.evaluate_query(query_samples(querysample), 'employee_id,count(*)', db_variables('database'),
                                        db_tables(tabletouse), 'employee_id', 'count(*)>1')
    pd = DbLib().execute_sql(test_query)
    passed, rownum, rows = Helpers.check_number_of_rows(pd, expvalue)
    if not passed:
        LOGGER.error('{} has {} duplicates'.format(db_tables(tabletouse), rownum))
        LOGGER.error('\r\nFAILED ROWS:\r\n{}\r\n'.format(rows))
    assert passed, '{} has {} duplicates'.format(db_tables(tabletouse), rownum)


@pytest.mark.employees
@pytest.mark.tc2
@pytest.mark.parametrize("querysample, tabletouse, expvalue",
                         [('TABLE_CHECKS_SQL_SELECT1', 'TRN_TABLE_EMPLOYEES', 0)
                          ])
def test_salary_is_positive_for_all_employees(querysample, tabletouse, expvalue):
    '''Case verifies that salary in hr.employees table is positive (>0) for all records
    *Test Steps:*
    1. Execute prepared query and migrate to pandas DataFrame
    2. Check number of rows returned is correct
    *Expected result:*
    1. Number of records returned by query is <=0
    2. Each returned records (Failed) must be logged
    '''
    allure.dynamic.title(f'Verified that in {db_tables(tabletouse)} '
                         f'salary is positive for all employees ')
    test_query = Helpers.evaluate_query(query_samples(querysample), 'employee_id,salary', db_variables('database'),
                                        db_tables(tabletouse), 'salary <= 0')
    pd = DbLib().execute_sql(test_query)
    passed, rownum, rows = Helpers.check_number_of_rows(pd, expvalue)
    if not passed:
        LOGGER.error('{} has {} rows with non-positive salary'.format(db_tables(tabletouse), rownum))
        LOGGER.error('\r\nFAILED ROWS:\r\n{}\r\n'.format(rows))
    assert passed, '{} has {} rows with non-positive salary'.format(db_tables(tabletouse), rownum)
