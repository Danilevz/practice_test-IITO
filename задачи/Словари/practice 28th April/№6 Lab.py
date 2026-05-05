friends={}
n=int(input('enter quantity of friends: '))
for i in range(n):
    name = input('enter name of a friend: ')
    age = int(input('enter age of a friend: '))
    friends[f'friend{i+1}'] = {'name': name, 'age': age}

print(friends)
all_ages = [inf['age'] for inf in friends.values()]
min_age = min(all_ages)

print(f"Младший друг: {min_age}, {name}")