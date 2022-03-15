import time

from pytest import mark
@mark.smoke
@mark.body

def test_body_functions_as_expected():
    assert True

@mark.bumper
def test_bumper():
    assert True

@mark.windshield
def test_windshield():
    assert True

@mark.ui
def test_can_navigate_to_body_page(chrome_browser):
    chrome_browser.get('https://www.motortrend.com/')
    time.sleep(5)
