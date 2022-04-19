stock_a = {"Samsung" : 22200, "LG" : 10800}

stock_b = {
    "Samsung": [20000, 25200, 19880, 24240, 21950],
    "LG" : (10800, 12600, 11150, 13760, 11420)
}

# be possible to overlap
stock_c = {
    "Samsung" : {
        "NOW" : 23000,
        "possession amount" : 5,
        "buying price" : 20000
    }
}

print(stock_a)
print(stock_b)
print(stock_c)

# Access Dictionary
print(stock_a["LG"])
print(stock_c["Samsung"]["possession amount"])

# Assign Dictionary
stock_a["Samsung"] = 24010
print(stock_a)

# delete Dictionary
del stock_a["LG"]
print(stock_a)

# Dictionary Function
stock_d = {
    "Naver" : 55500,
    "KaKao" : 10340,
    "BMW" : 115990,
    "BurgerKing" : 32330
}

# item : key and data pairs
print(stock_d.items())

# combine with "for"
for item in stock_d.items():
    print(item[0])
    
# keys() : key
for key in stock_d.keys():
    print(key)
    
# values() : data
for value in stock_d.values():
    print(value)    