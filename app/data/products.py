PRODUCTS = [
    {
        "id": 1,
        "name": "Coca-Cola 500ml",
        "category": "Bebidas",
        "price": 1800,
        "description": "Gaseosa individual fría",
        "stock": 20,
        "image_url": "https://example.com/coca-cola-500ml.png"
    },
    {
        "id": 2,
        "name": "Agua mineral 500ml",
        "category": "Bebidas",
        "price": 1200,
        "description": "Agua sin gas",
        "stock": 30,
        "image_url": "https://example.com/agua-500ml.png"
    },
    {
        "id": 3,
        "name": "Alfajor triple chocolate",
        "category": "Golosinas",
        "price": 950,
        "description": "Alfajor triple bañado en chocolate",
        "stock": 25,
        "image_url": "https://example.com/alfajor-triple.png"
    },
    {
        "id": 4,
        "name": "Papas fritas clásicas",
        "category": "Snacks",
        "price": 1600,
        "description": "Paquete individual de papas fritas",
        "stock": 18,
        "image_url": "https://example.com/papas-clasicas.png"
    },
    {
        "id": 5,
        "name": "Chocolate con maní",
        "category": "Golosinas",
        "price": 1300,
        "description": "Barra de chocolate con maní",
        "stock": 15,
        "image_url": "https://example.com/chocolate-mani.png"
    },
    {
        "id": 6,
        "name": "Sandwich de miga jamón y queso",
        "category": "Comidas",
        "price": 2500,
        "description": "Sandwich listo para consumir",
        "stock": 10,
        "image_url": "https://example.com/sandwich-miga.png"
    }
]


def get_all_products():
    return PRODUCTS


def get_product_by_id(product_id):
    for product in PRODUCTS:
        if product["id"] == product_id:
            return product
    return None
