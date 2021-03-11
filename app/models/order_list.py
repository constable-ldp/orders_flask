from app.models.order import *

order1 = Order(1, 'John', '03/03/2021', ['His Dark Materials', 'Harry Potter'], 2, 9.98)
order2 = Order(2, 'Mary', '05/03/2021', ['The Great Gatsby'], 1, 4.99)
order3 = Order(3, 'Luke', '06/03/2021', ['The Old Man and the Sea', 'On The Road', 'Harry Potter'], 3, 14.97)

orders = [order1, order2, order3]
