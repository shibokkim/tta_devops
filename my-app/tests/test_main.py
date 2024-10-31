# from my_app.main import add

# def test_add():
#     assert add(2, 3) == 5
#     assert add(-1, 1) == 0
#     assert add(0, 0) == 0
    
from fastapi.testclient import TestClient
from my_app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_item():
    response = client.get("/items/1?q=test")
    assert response.status_code == 404
    assert response.json() == {"item_id": 1, "query": "test"}