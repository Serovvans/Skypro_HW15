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
    user = User(**data)

    return user


@app.route("/users/<int:pk>", methods=["DELETE"])
def page_delete_user(pk):
    db.session.query(User).get(pk).delete()


@app.route("/orders", methods=['POST'])
def page_add_orders():
    data = request.json
    add_new_data_to_db([Order(**data)])

    return data


@app.route("/orders/<int:pk>", methods=["PUT"])
def page_update_order(pk):
    data = request.json
    order = db.session.query(Order).get(pk)
    order = Order(**data)

    return order


@app.route("/orders/<int:pk>", methods=["DELETE"])
def page_delete_order(pk):
    db.session.query(Order).get(pk).delete()


@app.route("/offers", methods=['POST'])
def page_add_offers():
    data = request.json
    add_new_data_to_db([Offer(**data)])

    return data


@app.route("/offers/<int:pk>", methods=["PUT"])
def page_update_offer(pk):
    data = request.json
    offer = db.session.query(Offer).get(pk)
    offer = Offer(**data)

    return offer


@app.route("/offers/<int:pk>", methods=["DELETE"])
def page_delete_offer(pk):
    db.session.query(Offer).get(pk).delete()


if __name__ == "__main__":
    app.run()
