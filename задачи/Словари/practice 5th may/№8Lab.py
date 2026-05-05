slova = {'компьютер':'pc', 'видеокарта':'graphics card', 'процессор':'cpu',
         'материнская плата':'motherboard', 'блок питания':'power block', 
         'оперативная память':'ram','корпус':'case', 'система охлаждения':'`vents'}
print('слова компьютерной тематики с доступным переводом: ')
print(slova.keys())
choice=input('enter word in russian which u wanna see translation of: ')
result=slova.get(choice, '__Error: entered word is not in a list__')
print('Translation of ur word: ',result)