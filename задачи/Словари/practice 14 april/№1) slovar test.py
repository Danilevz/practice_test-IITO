user=dict()
user['name']=input('enter name__')
user['surname']=input('enter surname__')
user['age']=int(input('enter age__'))
user['kurs']=input('enter kurs__')
print(user)
user.setdefault('group', 'IITO')
print(user)
user['age']=19
print(user)
user['kurs']=2
print(user)
del user['age']
print(user)
user.setdefault('email', None)
print(user)