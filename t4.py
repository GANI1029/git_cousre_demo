from ecommerceapp import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    user_role = db.Column(db.Integer, db.ForeignKey('role.role_id'), nullable=False)

    def _repr_(self):
        return f"<User {self.user_name}>"

class Role(db.Model):
    role_id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(50), unique=True, nullable=False)
    users = db.relationship('User', backref='role')

    def _repr_(self):
        return f"<Role {self.role_name}>"

class Category(db.Model):
    category_id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Product', backref='category')

    def _repr_(self):
        return f"<Category {self.category_name}>"

class Product(db.Model):
    product_id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float, nullable=False)
    product_name = db.Column(db.String(80), unique=True, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))

    def _repr_(self):
        return f"<Product {self.product_name}>"

class Cart(db.Model):
    cart_id = db.Column(db.Integer, primary_key=True)
    total_amount = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)

    def _repr_(self):
        return f"<Cart {self.cart_id}>"

class CartProduct(db.Model):
    cp_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.product_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def _repr_(self):
        return f"<CartProduct {self.cp_id}>"


####################

INSERT INTO role (role_name) VALUES ('CONSUMER'), ('SELLER');

INSERT INTO user (user_name, password, user_role)
VALUES ('jack', 'pass_word', 1),
       ('bob', 'pass_word', 2),
       ('apple', 'pass_word', 2),
       ('glaxo', 'pass_word', 2);

INSERT INTO category (category_name)
VALUES ('Fashion'),
       ('Electronics'),
       ('Books'),
       ('Groceries'),
       ('Medicines');

INSERT INTO product (price, product_name, category_id, seller_id)
VALUES (29190, 'ipad', 2, 3),
       (10, 'crocin', 5, 4);

INSERT INTO cart (total_amount, user_id)
VALUES (0, 1),
       (0, 2);

INSERT INTO cart_product (cart_id, product_id, quantity)
VALUES (1, 2, 2),
       (2, 1, 20);

