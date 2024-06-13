from user import User
from product import Product


User.create_table()
Product.create_table()

user1 = User( 'admin', 'admin')
user1.save()
user2 = User('user1', 'password1')
user2.save()

user1_retrieved = User.get_by_id(user1.user_id)
user1_retrieved.username == 'admin'
user1_retrieved.password == 'admin'

user2_retrieved = User.get_by_id(user2.user_id)
user2_retrieved.username == 'user1'
user2_retrieved.password == 'password1'


product1 = Product( 'Product 1 ', 10.99)
product1.save()
product2 = Product( 'Product 2' , 20.99)
product2.save()

product1_retrieved = Product.get_by_id(product1.id)
product1_retrieved.name == 'Product 1'
product1_retrieved.price == 10.99

product2_retrieved = Product.get_by_id(product2.id)
product2_retrieved.name == 'Product 2'
product2_retrieved.price == 20.99

Product.drop_table()

