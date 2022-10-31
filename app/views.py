from app import db
from flask import jsonify, request
from models import User, Offer, Order
from create_app import add_new_data_to_db, app


@app.route("/users")
def page_users():
    users = db.session.query(User).all()
    list_users = []
    for user in users:
        list_users.append(user.return_data())

    return jsonify(list_users)


@app.route("/users/<int:pk>")
def page_user_by_pk(pk: int):
    user = db.session.query(User).get(pk)
    dict_user = user.return_data()

    return jsonify(dict_user)


@app.route("/orders")
def page_orders():
    orders = db.session.query(Order).all()
    list_orders = []
    for order in orders:
        list_orders.append(order.return_data())

    return jsonify(list_orders)


@app.route("/orders/<int:pk>")
def page_order_by_pk(pk: int):
    order = db.session.query(Order).get(pk)
    dict_order = order.return_data()

    return jsonify(dict_order)


@app.route("/offers")
def page_offers():
    offers = db.session.query(Offer).all()
    list_offers = []
    for offer in offers:
        list_offers.append(offer.return_data())

    return jsonify(list_offers)


@app.route("/offers/<int:pk>")
def page_offer_by_pk(pk: int):
    offer = db.session.query(Offer).get(pk)
    dict_offer = offer.return_data()

    return jsonify(dict_offer)


@app.route("/users", methods=['POST'])
def page_add_users():
    data = request.json
    add_new_data_to_db([User(**data)])

    return data


@app.route("/users/<int:pk>", methods=["PUT"])
def page_update_user(pk):
    data = request.json
    user = db.session.query(User).get(pk)
    try:
        user.id = data.get("id")
        user.first_name = data.get("first_name")
        user.last_name = data.get("last_name")
        user.age = data.get("age")
        user.email = data.get("email")
        user.role = data.get("role")
        user.phone = data.get("phone")
    except Exception as e:
        print(e)
    db.session.commit()

    return user.return_data()


@app.route("/users/<int:pk>", methods=["DELETE"])
def page_delete_user(pk):
    user = db.session.query(User).get(pk)
    db.session.delete(user)
    db.session.commit()

    return {}


@app.route("/orders", methods=['POST'])
def page_add_orders():
    data = request.json
    add_new_data_to_db([Order(**data)])

    return data


@app.route("/orders/<int:pk>", methods=["PUT"])
def page_update_order(pk):
    data = request.json
    order = db.session.query(Order).get(pk)
    try:
        order.id = data.get("id")
        order.name = data.get("name")
        order.description = data.get("description")
        order.start_date = data.get("start_date")
        order.end_date = data.get("end_date")
        order.address = data.get("address")
        order.price = data.get("price")
        order.customer_id = data.get("customer_id")
        order.executor_id = data.get("executor_id")
    except Exception as e:
        print(e)
    db.session.commit()

    return order.return_data()


@app.route("/orders/<int:pk>", methods=["DELETE"])
def page_delete_order(pk):
    order = db.session.query(Order).get(pk)
    db.session.delete(order)
    db.session.commit()

    return {}


@app.route("/offers", methods=['POST'])
def page_add_offers():
    data = request.json
    add_new_data_to_db([Offer(**data)])

    return data


@app.route("/offers/<int:pk>", methods=["PUT"])
def page_update_offer(pk):
    data = request.json
    offer = db.session.query(Offer).get(pk)
    try:
        offer.id = data.get("id")
        offer.order_id = data.get("order_id")
        offer.executor_id = data.get("executor_id")
    except Exception as e:
        print(e)
    db.session.commit()

    return offer.return_data()


@app.route("/offers/<int:pk>", methods=["DELETE"])
def page_delete_offer(pk):
    offer = db.session.query(Offer).get(pk)
    db.session.delete(offer)
    db.session.commit()

    return {}


if __name__ == "__main__":
    app.run()
