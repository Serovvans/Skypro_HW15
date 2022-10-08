import json

from flask import Flask
from app import db
from models import User, Offer, Order


app = Flask(__name__)


def add_data_to_db():
    """Заполняем базу данными"""
    with open("../data/users.json", encoding="UTF-8") as users_data:
        list_users = json.load(users_data)

    users = []
    for user in list_users:
        users.append(User(id=user.get('id'), first_name=user.get('first_name'), last_name=user.get('last_name'),
                          age=user.get('age'), email=user.get('email'), role=user.get('role'), phone=user.get('phone'))
                     )

    orders = []
    with open("../data/orders.json", encoding="UTF-8") as orders_data:
        list_orders = json.load(orders_data)

    for order in list_orders:
        orders.append(Order(id=order['id'], name=order['name'], description=order['description'],
                            start_date=order['start_date'], end_date=order['end_date'], address=order['address'],
                            price=order['price'], customer_id=order['customer_id'], executor_id=order['executor_id'])
                      )

    offers = []
    with open("../data/offers.json", encoding="UTF-8") as offers_data:
        list_offers = json.load(offers_data)

    for offer in list_offers:
        offers.append(Offer(id=offer['id'], order_id=offer['order_id'], executor_id=offer['executor_id']))

    db.session.add_all(users)
    db.session.add_all(orders)
    db.session.add_all(offers)

    db.session.commit()


def create_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory:"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
        add_data_to_db()

    return app


app = create_app()


def add_new_data_to_db(data):
    db.session.add_all(data)
    db.session.commit()

