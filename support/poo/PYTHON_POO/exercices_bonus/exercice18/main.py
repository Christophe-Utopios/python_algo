# Création des tables
Base.metadata.create_all(bind=engine)

def add_order(session, customer_name):
    order = Order(customer_name=customer_name)
    session.add(order)
    session.commit()
    print(f"Commande ajoutée : {order.customer_name} à la date {order.date}")

def get_all_orders(session):
    orders = session.query(Order).all()
    for order in orders:
        print(f"ID: {order.id}, Client: {order.customer_name}, Total: {order.total_price}, Date: {order.date}")
    return orders

def update_order(session, order_id, new_customer_name):
    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        order.customer_name = new_customer_name
        session.commit()
    else:
        print(f"Commande avec ID {order_id} introuvable.")

def delete_order(session, order_id):
    order = session.query(Order).filter(Order.id == order_id).first()
    if order:
        session.delete(order)
        session.commit()
        print(f"Commande ID {order_id} supprimée.")
    else:
        print(f"Commande avec ID {order_id} introuvable.")


def add_product(session, name, price, quantity, order_id):
    product = Product(name=name, price=price, quantity=quantity, order_id=order_id)
    session.add(product)
    session.commit()

    print(f"Produit ajouté : {product.name}, Prix : {product.price}, Quantité : {product.quantity}, Commande ID : {product.order_id}")


def get_all_products(session):
    products = session.query(Product).all()
    for product in products:
        print(f"ID: {product.id}, Nom: {product.name}, Prix: {product.price}, Quantité: {product.quantity}, Commande ID: {product.order_id}")
    return products

def update_product(session, product_id, new_name=None, new_price=None, new_quantity=None):
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        order = session.query(Order).filter(Order.id == product.order_id).first()

        if new_name:
            product.name = new_name
        if new_price:
            product.price = new_price
        if new_quantity:
            product.quantity = new_quantity

        session.commit()
        print(f"Produit mis à jour : {product.name}, Prix : {product.price}, Quantité : {product.quantity}")
    else:
        print(f"Produit avec ID {product_id} introuvable.")

def delete_product(session, product_id):
    product = session.query(Product).filter(Product.id == product_id).first()
    if product:
        session.delete(product)
        session.commit()
        print(f"Produit ID {product_id} supprimé.")
    else:
        print(f"Produit avec ID {product_id} introuvable.")