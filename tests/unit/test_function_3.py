from functions.lambda_function_1 import app


def test_function_1():
    data = app.lambda_handler("", "")

    assert "code" in data
    assert "message" in data

    assert data["code"] == "500"
    assert data["message"] == "Internal Error"
