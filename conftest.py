import pytest
from datetime import datetime
from pathlib import Path
import shutil

'''
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    test_fn = item.obj
    docstring = getattr(test_fn, '__doc__')
    if docstring:
        report.nodeid = docstring
'''



@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # set custom options only if none are provided from command line
    #if not hasattr(config.option, 'log_file'):
    if config.option.log_file is None:
        now = datetime.now()
        reports_dir = Path('../reports', now.strftime('%Y%m%d'))
        reports_dir.mkdir(parents=True, exist_ok=True)
        config.option.log_file = 'reports/{}/log_failed_{}.log'.format(reports_dir,now.strftime('%Y%m%d%H%M'))
    '''
    if not hasattr(config.option,'htmlpath'):
        now = datetime.now()
        # create report target dir
        reports_dir = Path('../reports', now.strftime('%Y%m%d'))
        reports_dir.mkdir(parents=True, exist_ok=True)
        # custom report file
        report = reports_dir / f"report_{now.strftime('%H%M')}.html"
        # adjust plugin options
        config.option.htmlpath = report
        config.option.self_contained_html = True
    '''