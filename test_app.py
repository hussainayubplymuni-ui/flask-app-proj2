from app import app


def test_add():
    client = app.test_client()
    response = client.get('/add?a=10&b=20')

    assert response.status_code == 200
    assert response.json == {"result": 30.0}


def test_subtract():
    client = app.test_client()
    response = client.get('/subtract?a=50&b=20')

    assert response.status_code == 200
    assert response.json == {"result": 30.0}


def test_multiply():
    client = app.test_client()
    response = client.get('/multiply?a=10&b=5')

    assert response.status_code == 200
    assert response.json == {"result": 50.0}


def test_divide():
    client = app.test_client()
    response = client.get('/divide?a=100&b=20')

    assert response.status_code == 200
    assert response.json == {"result": 5.0}
def test_missing_numbers():
    client = app.test_client()
    response = client.get('/add?a=10')

    assert response.status_code == 400
    assert response.json == {"error": "Both numbers are required"}


def test_invalid_numbers():
    client = app.test_client()
    response = client.get('/add?a=hello&b=20')

    assert response.status_code == 400
    assert response.json == {"error": "Please enter valid numbers"}


def test_divide_by_zero():
    client = app.test_client()
    response = client.get('/divide?a=10&b=0')

    assert response.status_code == 400
    assert response.json == {"error": "Cannot divide by zero"}
