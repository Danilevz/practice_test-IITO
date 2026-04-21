a=int(input('enter natural number'))
sl= {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
astr=str(a)
result=' '.join(sl[digit] for digit in astr)
print(result)