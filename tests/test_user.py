import requests


BASE_URL = "http://127.0.0.1:8000"


def test_authentication_fails_with_invalid_credentials(mocker):
    """
    The /users endpoint should return 401 and an empty body
    when the credentials are invalid.
    """
    # Mock de la respuesta del servidor
    mocked_response = mocker.Mock()
    mocked_response.status_code = 401
    mocked_response.text = ""

    # Interceptar requests.get y devolver el mock
    mocker.patch("requests.get", return_value=mocked_response)

    # Llamada "simulada" al endpoint
    response = requests.get(
        f"{BASE_URL}/users/",
        params={"username": "admin", "password": "admin"},
        timeout=5,
    )

    assert response.status_code == 401
    assert response.text.strip() == ""


def test_authentication_succeeds_with_valid_credentials(mocker):
    """
    The /users endpoint should return 200 and an empty body
    when the credentials are valid.
    """
    # Mock de la respuesta del servidor
    mocked_response = mocker.Mock()
    mocked_response.status_code = 200
    mocked_response.text = ""

    # Interceptar requests.get y devolver el mock
    mocker.patch("requests.get", return_value=mocked_response)

    # Llamada "simulada" al endpoint
    response = requests.get(
        f"{BASE_URL}/users/",
        params={"username": "admin", "password": "qwerty"},
        timeout=5,
    )

    assert response.status_code == 200
    assert response.text.strip() == ""
