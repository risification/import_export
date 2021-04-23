data = [
    {'dress': [
        {'name': 'louis vuitton',
         'popularity': 500,
         'price': 1000
         },
        {'name': 'versace',
         'popularity': 21,
         'price': 888
         },
        {'name': 'supreme',
         'popularity': 57,
         'price': 7650000
         },
    ]
    },
    {'jeans': [
        {'name': 'adidas',
         'popularity': 42,
         'price': 2300
         },
        {'name': 'armani',
         'popularity': 671111118,
         'price': 110
         },
        {'name': 'casio',
         'popularity': 230,
         'price': 3000
         },
    ]
    },
    {'t-shirt': [
        {'name': 'tom ford',
         'popularity': 999,
         'price': 5000
         },
        {'name': 'lacoste',
         'popularity': 777,
         'price': 230
         },
        {'name': 'luxury',
         'popularity': 876,
         'price': 2300
         },
    ]
    }
]

# print(data[0]['dress'])
sum = 0
sum1 = 0
sum2 = 0
for i in data:
    for key_category in i:
        for dict_product in i[key_category]:
            if key_category == 'dress':
                sum += dict_product['popularity']
            elif key_category == 'jeans':
                sum1 += dict_product['popularity']
            elif key_category == 't-shirt':
                sum2 += dict_product['popularity']

if sum > sum1 and sum > sum2:
    a = {'most_popular_category_dress': sum}
    print(a)
elif sum1 > sum and sum1 > sum2:
    a = {'most_popular_category_jeans': sum1}
    print(a)
elif sum2 > sum and sum2 > sum1:
    a = {'most_popular_category_t-shirt': sum2}
    print(a)

sum = 0
sum1 = 0
sum2 = 0
for i in data:
    for key_category in i:
        for dict_product in i[key_category]:
            if key_category == 'dress':
                sum += dict_product['price']
            elif key_category == 'jeans':
                sum1 += dict_product['price']
            elif key_category == 't-shirt':
                sum2 += dict_product['price']

if sum > sum1 and sum > sum2:
    a = {'most_price_category_dress': sum}
    print(a)
elif sum1 > sum and sum1 > sum2:
    a = {'most_price_category_jeans': sum1}
    print(a)
elif sum2 > sum and sum2 > sum1:
    a = {'most_price_category_t-shirt': sum2}
    print(a)
name_list = []
dictionary = {}
list1 = []
for i in data:
    for key_category in i:
        for dict_product in i[key_category]:
            b = dict_product['price']
            name = name_list.append(dict_product['name'])
            a = list1.append(b)
            i = 0
            while i < len(list1):
                dictionary[name_list[i]]=list1[i]
                i +=1
print(max(dictionary,key=dictionary.get),':')
print(dictionary[max(dictionary,key=dictionary.get)])
print(min(dictionary,key=dictionary.get),':')
print(dictionary[min(dictionary,key=dictionary.get)])