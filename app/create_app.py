import json

from flask import Flask
from app import db
from models import User, Offer, Order


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///:memory"
    #app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()
        add_data_to_db()

    return app


app = create_app()


def add_data_to_db():
    """Заполняем базу данными"""
    users = {}
    with open("data/users.json", encoding="UTF-8") as users_data:
        list_users = json.load(users_data)

    for user in list_users:
        users[user["id"]] = User(id=user['id'], first_name=user['first_name'], last_name=user['last_name'],
                                 age=user['age'], email=user['email'], role=user['role'], phone=user['phone'])

    orders = {}
    with open("data/orders.json", encoding="UTF-8") as orders_data:
        list_orders = json.load(orders_data)

    for order in list_orders:
        orders[order['id']] = Order(id=order['id'], name=order['name'], start_date=order['start_date'],
                                    end_date=order['end_date'], address=order['address'], price=order['price'],
                                    customer=users[order['customer_id']], executor=users[order['executor_id']])

    offers = []
    with open("data/offers.json", encoding="UTF-8") as offers_data:
        list_offers = json.load(offers_data)

    for offer in list_offers:
        offers.append(Offer(id=offer['id'], order=orders[offer['order_id']], executor=users[offer['executor_id']]))

    db.session.add_all(users.values())
    db.session.add_all(orders.values())
    db.session.add_all(offers)

    db.session.commit()


def add_new_data_to_db(data):
    db.session.add_all(data)
    db.session.commit()

