import pytest
from decouple import config


@pytest.mark.test_login_page
@pytest.mark.parametrize(
    "email, password, validity",
    [
        (config('USER_EMAIL'), "wrong_password", None),  # Bad request(wrong password)
        ("wrong_email@gmail.com", config('USER_PASSWORD'), None),  # Bad request(wrong email)
        ("invalid_email_format", config('USER_PASSWORD'), None),  # Bad request(invalid email format)        
        (config('USER_EMAIL'), config('USER_PASSWORD'), True),
    ]
)
def test_user_login(user_login_fixture, email, password, validity):
    login_page = user_login_fixture
    assert login_page.click_login_form() is not None
    assert login_page.verify_login_page() is not None
    assert login_page.enter_email(email) is not None
    assert login_page.enter_password(password) is not None
    assert login_page.click_login_button() is not None
    if validity:
        assert login_page.verify_successfull_login() is not None
    else:
        assert login_page.wrong_email_or_password() is not None
        login_page.key_code(4)