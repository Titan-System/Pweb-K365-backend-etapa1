import pytest

from app import create_app
from app.services.cart_service import clear_cart


@pytest.fixture()
def client():
    app = create_app()
    app.config.update({"TESTING": True})

    clear_cart()
    with app.test_client() as client:
        yield client
    clear_cart()


def test_health_check(client):
    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_list_products(client):
    response = client.get("/api/products")
    data = response.get_json()

    assert response.status_code == 200
    assert "products" in data
    assert len(data["products"]) >= 1


def test_get_product_by_id(client):
    response = client.get("/api/products/1")
    data = response.get_json()

    assert response.status_code == 200
    assert data["product"]["id"] == 1


def test_get_product_not_found(client):
    response = client.get("/api/products/999")

    assert response.status_code == 404


def test_add_item_to_cart(client):
    response = client.post("/api/cart/items", json={"product_id": 1, "quantity": 2})
    data = response.get_json()

    assert response.status_code == 201
    assert data["items_count"] == 2
    assert data["items"][0]["product"]["id"] == 1
    assert data["items"][0]["quantity"] == 2


def test_add_same_item_increments_quantity(client):
    client.post("/api/cart/items", json={"product_id": 1, "quantity": 1})
    response = client.post("/api/cart/items", json={"product_id": 1, "quantity": 2})
    data = response.get_json()

    assert response.status_code == 201
    assert data["items_count"] == 3
    assert data["items"][0]["quantity"] == 3


def test_add_invalid_product_returns_404(client):
    response = client.post("/api/cart/items", json={"product_id": 999, "quantity": 1})

    assert response.status_code == 404


def test_add_invalid_quantity_returns_400(client):
    response = client.post("/api/cart/items", json={"product_id": 1, "quantity": 0})

    assert response.status_code == 400


def test_cart_total(client):
    client.post("/api/cart/items", json={"product_id": 1, "quantity": 2})
    response = client.get("/api/cart/total")
    data = response.get_json()

    assert response.status_code == 200
    assert data["total"] == 3600
    assert data["items_count"] == 2


def test_remove_item_from_cart(client):
    client.post("/api/cart/items", json={"product_id": 1, "quantity": 1})
    response = client.delete("/api/cart/items/1")
    data = response.get_json()

    assert response.status_code == 200
    assert data["items_count"] == 0
    assert data["total"] == 0


def test_clear_cart(client):
    client.post("/api/cart/items", json={"product_id": 1, "quantity": 1})
    client.post("/api/cart/items", json={"product_id": 2, "quantity": 1})

    response = client.delete("/api/cart")
    data = response.get_json()

    assert response.status_code == 200
    assert data["items"] == []
    assert data["total"] == 0
    assert data["items_count"] == 0
