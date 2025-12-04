#!/usr/bin/env python3

import sys
import json


s = 0
sn = 0
n = 1
product_qty = []

for data in sys.stdin:
    json_data = json.loads(data)
    print('block %s:' % n)
    print('total income: \t%s' % json_data['total_income'])
    print('transactions: \t%s' % json_data['count'])
    print('average: \t%s' % json_data['average'])
    print('=======')
    print('most sold products:')
    print('=======')
    print('name\tqty')
    for p in json_data['products']:
        print('%s\t%s' % (p['product'], p['qty']))
    print('')
    s += float(json_data['total_income'])
    sn += float(json_data['count'])
    n += 1

    if not product_qty:
        product_qty.extend(json_data['products'])
    else:
        for p in json_data['products']:
            product_qty = list(map(lambda x: {
                'product': x['product'],
                'qty': x['qty'] + (0 if x['product'] != p['product'] else p['qty'])
            }, product_qty))

print('total:')
print('total income: \t%s' % s)
print('transactions: \t%s' % sn)
print('average: \t%s' % float(s/sn))
print('=======')
print('most sold products:')
print('=======')
print('name\tqty')
for p in list(sorted(product_qty, key=lambda x: x['qty'], reverse=True)):
    print('%s\t%s' % (p['product'], p['qty']))
