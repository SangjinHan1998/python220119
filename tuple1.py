a = (30,)
# if you want to have one data tuple, Insert comma.

b = tuple([5,6,7])
print(b)

x = list(range(10))
c = tuple(x)
# list --> tuple 
print(c)

x1 = 5, 6, 7
d = list(x1)
# tuple --> list
print(d)

numbers = 3, 4, 5 
# 패킹. 여러 개의 데이터를 하나의 변수에 할당하는것 (assign several data in one variable)

a1, b1, c1 = numbers 
# 언패킹. 컬렉션의 각 데이터를 각각의 변수에 할당하는것 (assign each data in each variable)


# 튜플 함수. 
e = 10, 20, 30, 40, 50
# index
e.index(20)
# some
e.count(30)
# max / min
max(e) , min(e)
# sum
sum(e)

# Do not memory this concept. Just understand.


