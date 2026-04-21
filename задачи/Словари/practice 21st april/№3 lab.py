a=int(input('enter number of ur course for info__'))
if a>4:
    print('error^ info only for programs with 4 courses innem__')
    exit()
kurses={'1':'First course is the beginning of your education. Here u will learn basic stuff necesarry for ur next courses',
        '2':'Second course is where u gonna go deeper into lerning ur professionaly required disciplines',
        '3':'Third course goes even further into learning what u will need on ur future work, practises may begin here',
        '4':'U likely learned all u will need at this point so ur just practicing and getting ready for ur corse final work'}
if a==1:
    print(kurses['1'])
if a==2:
    print(kurses['2'])
if a==3:
    print(kurses['3'])
if a==4:
    print(kurses['4'])
