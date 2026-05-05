friends={}
n=int(input('enter quantity of friends: '))
for i in range(n):
    name = input('enter name of a friend: ')
    age = int(input('enter age of a friend: '))
    friends['friend {}'.format(i+1)] = {'name': name, 'age': age}

print(friends)
all_ages = [inf['age'] for inf in friends.values()]
all_names = [inf['name'] for inf in friends.values()]
name_and_age = dict(zip(all_names, all_ages))
min_age_name = min(name_and_age, key=name_and_age.get)
print("youngest friend: {}, {}".format(name_and_age[min_age_name], min_age_name))
def comm_age(n, all_ages): #i dunno why i did this as function, like, i could do it w/o it but it works so its alr
    s=sum(all_ages)
    sr_age=s/n
    return sr_age
print('common age of friends: ',comm_age(n, all_ages))
len_names = [len(i) for i in all_names]
name_andlen = dict(zip(all_names,len_names))
longest_name = max(name_andlen, key=name_andlen.get)
print('friend with longest name: {}, {}'.format(name_andlen[longest_name], longest_name))