def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Expense Tracker" in response.data

def test_add(client):
    response = client.post("/add", data={
        "title": "Coffee", "amount": "50",
        "category": "Food", "kind": "expense"
    }, follow_redirects=True)
    assert response.status_code == 200
    assert b"Coffee" in response.data

def test_api(client):
    response = client.get("/api/transactions")
    assert response.status_code == 200
