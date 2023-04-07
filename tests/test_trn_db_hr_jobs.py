import pytest
import allure
from libs.helpers.libs import Helpers
from libs.helpers.dbLib import DbLib
from config.variables import *
from config.dbvariables import *
import logging

LOGGER = logging.getLogger(__name__)


@pytest.mark.jobs
@pytest.mark.tc3
@pytest.mark.parametrize("querysample, tabletouse, expvalue",
                         [('TABLE_CHECKS_SQL_SELECT1', 'TRN_TABLE_JOBS', 0)
                          ])
def test_min_salary_lessorequal_to_max_salary_in_jobs_table(querysample, tabletouse, expvalue):
    '''Case verifies that min_salary in hr.jobs table is less or equal to max_salary for all records
    *Test Steps:*
    1. Execute prepared query and migrate to pandas DataFrame
    2. Check number of rows returned is correct
    *Expected result:*
    1. Number of records returned by query is 0
    2. Each returned records (Failed) must be logged
    '''
    allure.dynamic.title(f'Verified that in {db_tables(tabletouse)} '
                         f'Min Salary is less or equal to Max Salary')
    test_query = Helpers.evaluate_query(query_samples(querysample), '*', db_variables('database'),
                                        db_tables(tabletouse),
                                        'min_salary is not null and max_salary is not null and min_salary > max_salary')
    pd = DbLib().execute_sql(test_query)
    passed, rownum, rows = Helpers.check_number_of_rows(pd, expvalue)
    if not passed:
        LOGGER.error('{} has {} rows having min_salary > max_salary'.format(db_tables(tabletouse), rownum))
        LOGGER.error('\r\nFAILED ROWS:\r\n{}\r\n'.format(rows))
    assert passed, '{} has {} rows having min_salary > max_salary'.format(db_tables(tabletouse), rownum)


@pytest.mark.jobs
@pytest.mark.tc4
@pytest.mark.parametrize("querysample, tabletouse, expvalue",
                         [('TABLE_CHECKS_SQL_SELECT0', 'TRN_TABLE_JOBS', 0)
                          ])
def test_min_job_id_job_title_pairs_have_expected_values(querysample, tabletouse, expvalue):
    '''Case verifies that all combinations job_id+job_title in Jobs table have predefned values
    *Test Steps:*
    1. Execute prepared query and migrate to pandas DataFrame
    2. Compare result to the predefined expected result
    *Expected result:*
    1. Number of mismatches is 0
    2. Each returned records (Failed) must be logged
    '''
    allure.dynamic.title(f'Verified that {db_tables(tabletouse)} '
                         f'table has expected job_id+job_title pairs')
    test_query = Helpers.evaluate_query(query_samples(querysample), 'job_id,job_title', db_variables('database'),
                                        db_tables(tabletouse))
    pd = DbLib().execute_sql(test_query)
    expecteddict = jobid_jobtitle_pairs()
    passed, rownum, rows = Helpers.check_all_records_correspond_dictionary(pd, expecteddict)
    if not passed:
        LOGGER.error('{} has {} unexpected job_id+job_title pairs'.format(db_tables(tabletouse), rownum))
        LOGGER.error('\r\nFAILED ROWS:\r\n{}\r\n'.format(rows))
    assert passed, '{} has {} unexpected job_id+job_title pairs'.format(db_tables(tabletouse), rownum)
