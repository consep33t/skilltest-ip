import json

with open('data1.json') as f:
    data = json.load(f)

march_orders = []

for order in data:
    order_date = order['created_at']
    if order_date[5:7] == '03':
        march_orders.append(order)

print(march_orders)
