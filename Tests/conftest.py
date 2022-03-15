import time
from pytest import fixture
from selenium import webdriver
from config import Config

def pytest_addoption(parser):
    parser.addoption('--env', action='store', default='', help='Environment that you want to test against')

@fixture(scope='session')
def app_config():
    cfg = Config(env)
    return cfg


@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')

@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome()
    yield browser

    # Teardown
    print('I am tearing down this browser')

