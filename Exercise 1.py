a = input('Enter a four-digit ticket number ')
b = len(a)
if b % 4:
    print('There is no such ticket.')
else:
    if int(a[0]) + int(a[1]) == int(a[2]) + int(a[3]):
        print('Happy ticket')
    else:
        print('Not a lucky ticket')