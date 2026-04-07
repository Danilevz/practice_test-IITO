user=dict()
user['name']=input('enter name')
user['surname']=input('enter surname')
user['age']=int(input('enter age'))
print(user)
user['age']=19
print(user)
del user['name']
print(user)
user.setdefault('email', None)
print(user)