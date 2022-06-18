 
from datetime import datetime
import json

products=input("Введите json с товарами:  ")
filter_for_products = []

for _ in range(5):
    s=input("Введите фильтр и его значение через пробел:  ").split()

    if s[0] in ['PRICE_GREATER_THAN', 'PRICE_LESS_THAN']:
        s[1] = int(s[1])
    if s[0] in ['DATE_AFTER', 'DATE_BEFORE']:
        s[1] = datetime.strptime(s[1], '%d.%m.%Y')
        
    filter_for_products.append(s)


data = json.loads(products)

for filter_one in filter_for_products:
    if filter_one[0] == "PRICE_GREATER_THAN":
        data = [i for i in data if i['price']>=filter_one[1]]
        continue

    if filter_one[0] == "PRICE_LESS_THAN":
        data = [i for i in data if i['price']<=filter_one[1]]
        continue

    if filter_one[0] == "DATE_AFTER":
        data = [i for i in data if datetime.strptime(i['date'], '%d.%m.%Y')>=filter_one[1]]
        continue

    if filter_one[0] == "DATE_BEFORE":
        data = [i for i in data if datetime.strptime(i['date'], '%d.%m.%Y')<=filter_one[1]]
        continue

    if filter_one[0] == "NAME_CONTAINS":
        data = [i for i in data if filter_one[1].lower() in i['name'].lower()]
        continue


res=sorted(data, key=lambda point: (point['id']))
print(json.dumps(res))

