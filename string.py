a = 'cuonghv Cuonghv'

b = a.ljust(50,'*')
print(b)
c = a.join(('1','2','3'))

d = a.replace('u', 'A', 2)
print(c)
print(d)
#Phan dau va phan cuoi bo di. hoac chu trong ngoac, lstrip, rstrip
e = a.strip('c')
print(e)