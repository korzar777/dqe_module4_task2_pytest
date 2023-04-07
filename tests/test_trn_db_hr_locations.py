import pytest
import allure
from libs.helpers.libs import Helpers
from libs.helpers.dbLib import DbLib
from config.variables import *
from config.dbvariables import *
import logging

LOGGER = logging.getLogger(__name__)

@pytest.mark.locations
@pytest.mark.tc5
@pytest.mark.parametrize("querysample, tabletouse, expvalue",
                         [('TABLE_CHECKS_SQL_SELECT1','TRN_TABLE_LOCATIONS', 0)
                          ])
def test_coutryids_with_bad_formatting_locations_table(querysample, tabletouse, expvalue):
    '''Case verifies that coutryid has correct formatting
    *Test Steps:*
    1. Execute prepared query and migrate to pandas DataFrame
    2. Check number of rows returned is correct
    *Expected result:*
    1. Number of records returned by query is 0
    2. Each returned records (Failed) must be logged
    '''
    allure.dynamic.title(f'Verified that {db_tables(tabletouse)} '
                         f'Coutryid columns has correct formatting. Checking: ID length is 2 symbols and uppercase')
    test_query = Helpers.evaluate_query(query_samples(querysample),'TRIM(country_id)',db_variables('database'),
                           db_tables(tabletouse),'len(TRIM(country_id))!=2 or upper(country_id) != country_id COLLATE Latin1_General_BIN2')
    pd = DbLib().execute_sql(test_query)
    passed, rownum, rows = Helpers.check_number_of_rows(pd,expvalue)
    if not passed:
        LOGGER.error('{} has {} coutryids with bad formatting'.format(db_tables(tabletouse),rownum))
        LOGGER.error('\r\nFAILED ROWS:\r\n{}'.format(rows))
    assert passed, '{} has {} coutryids with bad formatting'.format(db_tables(tabletouse),rownum)

@pytest.mark.locations
@pytest.mark.tc6
@pytest.mark.parametrize("querysample, tabletouse, expvalue",
                         [('TABLE_CHECKS_SQL_SELECT1','TRN_TABLE_LOCATIONS', 0)
                          ])
def test_adress_length_is_less_than_column_size_locations_table(querysample, tabletouse, expvalue):
    '''Case verifies that length of text in address column in hr.locations table is less than size of column
    Potentially this case can be issue. Treated as Failed if address length is the same as column length
    *Test Steps:*
    1. Execute prepared query and migrate to pandas DataFrame
    2. Check number of rows returned is correct
    *Expected result:*
    1. Number of records returned by query is 0
    2. Each returned records (Failed) must be logged
    '''
    allure.dynamic.title(f'Verified that for {db_tables(tabletouse)} '
                         f'length of text in address column in hr.locations table is less than size of column')
    test_query = Helpers.evaluate_query(query_samples(querysample),'location_id,street_address',db_variables('database'),
                           db_tables(tabletouse), 'len([street_address])>=40')
    pd = DbLib().execute_sql(test_query)
    passed, rownum, rows = Helpers.check_number_of_rows(pd, expvalue)
    if not passed:
        LOGGER.error('{} has {} rows with max allowed length of address'.format(db_tables(tabletouse),rownum))
        LOGGER.error('\r\nFAILED ROWS:\r\n{}\r\n'.format(rows))
    assert passed, '{} has {} rows with max allowed length of address'.format(db_tables(tabletouse),rownum)