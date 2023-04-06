import json

with open('data1.json') as f:
    data = json.load(f)

customer_totals = {}

for order in data:
    customer_name = order['customer']['name']
    total_price = 0
    for item in order['items']:
        total_price += item['price'] * item['qty']
    if total_price > 300000:
        if customer_name not in customer_totals:
            customer_totals[customer_name] = total_price
        else:
            customer_totals[customer_name] += total_price

result = [name for name, total in customer_totals.items() if total > 300000]
print("orang yang melakukan pembelian dengan total keseluruhan lebih dari 300.000 adalah :")
print(customer_totals)
