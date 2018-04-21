from app import *

def test_get_form():
    assert get_form({'login_email': 'test@ex.com', 'login_password':'safhsd'}) == {'login_email':'email', 'login_password':'text'}
    assert get_form({'login_email': 'test@ex.com', 'login_password':''}) == {'login_email':'email', 'login_password':'text'}
