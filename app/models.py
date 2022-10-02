from app import db
from sqlalchemy.orm import relationship


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.Text(200), nullable=True)
    last_name = db.Column(db.Text(200))
    age = db.Column(db.Integer)
    email = db.Column(db.Text(200))
    role = db.Column(db.Text(200))
    phone = db.Column(db.Text(200))

    def return_data(self):
        return {"id": self.id, "first_name": self.first_name, "last_name": self.last_name, "age": self.age,
                "email": self.email, "role": self.role, "phone": self.phone}


class Order(db.Model):
    __tablename__ = "order"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text(200))
    description = db.Column(db.Text(400))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    address = db.Column(db.Text(200))
    price = db.Column(db.Integer)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("executor.id"))

    customer = relationship("User")
    executor = relationship("User")

    def return_data(self):
        return {"id": self.id, "name": self.name, "start_date": self.start_date,
                "end_date": self.end_date, "address": self.address, "price": self.price,
                "customer_id": self.customer_id, "executor_id": self.executor_id}


class Offer(db.Model):
    __tablename__ = "offer"

    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey("order.id"))
    executor_id = db.Column(db.Integer, db.ForeignKey("executor.id"))

    order = relationship("Order")
    executor = relationship("User")

    def return_data(self):
        return {"id": self.id, "order_id": self.order_id, "executor_id": self.executor_id}
