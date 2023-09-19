from market import app

def test_given_app_when_accessing_home_page_expect_200():
    with app.test_client() as client:
        response = client.get('/home')
        assert response.status_code == 200

def test_given_app_when_accessing_non_existing_page_expect_404():
    with app.test_client() as client:
        response = client.get('/non_existing')
        assert response.status_code == 404

# check something aobut the db
# check when passing the user info it log. check with Admin info(correct and no correct passwords)