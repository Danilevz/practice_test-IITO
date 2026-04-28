relations={"usd": 80.0, 'eur': 90, 'cny': 11}
rub=int(input('enter quantity of rubles: '))
choice=input('enter to what value u want to convert: usd, eur, cny ')
if choice=='usd':
    print('your digits converted usd: ',rub*relations['usd'])
if choice=='eur':
    print('your digits converted eur: ',rub*relations['eur'])
if choice=='cny':
    print('your digits converted cny: ', rub*relations['cny'])