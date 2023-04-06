import json

with open('data1.json') as f:
    data = json.load(f)

annis_orders = []

for order in data:
    customer_name = order['customer']['name']
    if customer_name == 'Annis':
        annis_orders.append(order)

total_price = 0

for order in annis_orders:
    for item in order['items']:
        total_price += item['price'] * item['qty']
print("total keseluruhan harga barang annis :")
print(total_price)
