cuong = 'Cuong'
print(cuong)
cuong = 28
print(cuong )

# List trong ngoac vuong[]
a = [1,2,3,'Cuonghv'], [2,4,66,7]
print(a)
#List comprehension 
b = [ cuong for cuong in range(10)]
print(b)

# Tao bien trong cong thuc luon
c = [[n,n*1,n*2] for n in range(1,4)]
print(c)

#list(iterable)
d = list('Cuonghv')
print(d)

#Toan tu trong list (a+=... tuong duong voi a = a + ...)
f = [1,2]
f+=['one', 'two']
f*=2
print(f)
#Lay ra phan tu dau tien cua chuoi g
g = [1,2,'a','b','c',[3,4]]
h = g[0] #Lay tu vi tri 1 den vi tri thu 3 => g[1:6]
print(h)

#Thay doi noi dung list => goi phan tu can thay doi ra va gan gia tri moi cho no
g[1] = 'Cuonghv'
print(g)