from app.data.products import get_product_by_id

# Persistencia inicial en memoria.
# La clave es product_id y el valor es la cantidad agregada.
_CART_ITEMS = {}


def clear_cart():
    _CART_ITEMS.clear()


def add_item(product_id, quantity=1):
    product = get_product_by_id(product_id)

    if product is None:
        return None, "PRODUCT_NOT_FOUND"

    if not isinstance(quantity, int) or quantity <= 0:
        return None, "INVALID_QUANTITY"

    current_quantity = _CART_ITEMS.get(product_id, 0)
    new_quantity = current_quantity + quantity

    if new_quantity > product["stock"]:
        return None, "INSUFFICIENT_STOCK"

    _CART_ITEMS[product_id] = new_quantity
    return get_cart(), None


def remove_item(product_id):
    if product_id not in _CART_ITEMS:
        return None, "ITEM_NOT_IN_CART"

    del _CART_ITEMS[product_id]
    return get_cart(), None


def get_cart():
    items = []
    total = 0

    for product_id, quantity in _CART_ITEMS.items():
        product = get_product_by_id(product_id)
        if product is None:
            continue

        subtotal = product["price"] * quantity
        total += subtotal

        items.append({
            "product": product,
            "quantity": quantity,
            "subtotal": subtotal
        })

    return {
        "items": items,
        "total": total,
        "items_count": sum(_CART_ITEMS.values())
    }
