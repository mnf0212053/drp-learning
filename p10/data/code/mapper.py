#!/usr/bin/env python3

from functools import reduce
import sys
import json

total_income = 0
n = 0

product_qty = []

for data in sys.stdin:
    json_data = json.loads(data)
    total_income += json_data['price_subtotal']
    n += 1

    if not list(filter(lambda x: x['product'] == json_data['product'], product_qty)):
        product_qty.append({
            'product': json_data['product'],
            'qty': json_data['qty']
        })
    else:
        product_qty = list(map(lambda x: {
            'product': x['product'],
            'qty': x['qty'] + (0 if x['product'] != json_data['product'] else json_data['qty'])
        }, product_qty))

res = {
    "total_income": total_income,
    "count": n,
    "average": total_income/n,
    "products": list(sorted(product_qty, key=lambda x: x['qty'], reverse=True))
}

print(json.dumps(res))
