# month
m = int(input("Input month number: "))

if m==12 or m==1 or m==2:
    print('winter')
elif m>=3 and m<=11:
    print('not winter')
else:
    print('incorrect input')
