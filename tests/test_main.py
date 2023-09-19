from flask import Config

from market import app, db


class TestConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False


def test_given_app_when_accessing_home_page_expect_200():
    with app.test_client() as client:
        response = client.get('/home')
        assert response.status_code == 200


def test_given_app_when_accessing_non_existing_page_expect_404():
    with app.test_client() as client:
        response = client.get('/non_existing')
        assert response.status_code == 404


def test_given_wrong_user_info_to_login_when_calling_signin_in_the_main_page_then_the_login_page_should_appear_again():
    with app.test_client() as client:
        data = {'csrf_token': "csrf", 'username': 'Test', "password_hash": "1111111111", "submit": "Singin"}
        response = client.post('/login', data=data)
        assert response.status_code == 200
        assert "<label for=\"username\">Write here your user name:</label>" in response.get_data(as_text=True)


def test_given_request_to_login_correct_the_market_page_should_be_displayed():
    with app.test_client() as client:
        response = client.get('/market')
        assert response.status_code == 302


def test_():
    with app.test_client() as client:
        data = {'csrf_token': "csrf", 'username': 'Beatriz', "password_hash": "654321", "submit": "Singin"}
        response = client.post('/login', data=data)
        assert response.status_code == 200
        # assert "Add Items" in response.get_data(as_text= True)


# This test is not working for reruting the website to a different one ❌
def test_logout_redirect():
    with app.test_client() as client:
        response = client.get("/logout_page")
        # Check that there was one redirect response.
        assert len(response.history) == 1
        # Check that the second request was to the index page.
        assert response.request.path == "/home"


def test_landing_aliases():
    with app.test_client() as client:
        landing = client.get("/")
        assert client.get("/home").data == landing.data


