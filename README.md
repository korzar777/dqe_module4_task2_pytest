# DQE Module python project using pytest
Includes several DQE tests for TRN DB tables
Data is queried using sqlalchemy library, stored to pandas dataframes
Fails are logged to files and Allure report is generated  

## Project structure
- tests folder - contains test modules. Splitted by names of tables. 
- libs folder - contains core helpers (methods for working with database and processing data )
- config folder - contains test variables, configuration, testdata
- report - latest logs and allure reports (results of execution and generated html)

## Preparing environment for tests execution
```bash
python -m venv venv 
venv\Scripts\activate
pip install -r requirements.txt
```

## Run pytest tests
```bash
python -m pytest    ##to run all tests in module
python -m pytest  tests/test_trn_db_hr_employees.py  ##to run only employees table tests
python -m pytest -m employees   ##to run only tests marked as 'employees'
python -m pytest -m employees -m tc1  ##run only tests marked both as 'employees' AND 'tc1'
python -m pytest -k test_employees_has_no_duplicates  ##run specific test in testfile
```

## Reporting using Allure Framework
NOTE: allure application must be installed to use it see https://docs.qameta.io/allure/
```bash
python -m pytest  --alluredir=reports/allure-results  ##save Allure report results
#to generate and open report (based on execution results)
allure serve reports/allure-results      ##open allure report; allure server will be closed once report would be closed
# to generate report (based on execution results) and then open it 
allure generate reports/allure-results   ##generate html report from  allure-results to allure-report folder
allure open reports/allure-report
##other options
# - setup docker image from allure or using  Allure Jenkins Plugin in jenkins
```

# Pandas library integration with pytest Framework
For the integration library pandas library need to be installed
```bash
pip install pandas
```
