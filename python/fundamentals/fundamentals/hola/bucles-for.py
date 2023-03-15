#contador desde el 0 al 150
for i in range(151):
    print(i)
    ''''''
#de 5 en 5 hasta 1000
for i in range(5,1005,5):
    print(i)
    ''''''
#contar, a la manera del dojo
for i in range(1,101):
    if i % 10 == 0:
        print("coding dojo")
    elif i % 5 == 0:
        print("coding")
    else:
        print(i)
    ''''''
#Whoa. es un gran idiota
sum = 0
for i in range(1,500001,2):
    sum += i
print(sum)


''''''
#cuenta regresiva de 4 en 4
y = 2018
while y > 0:
    print(y)
    y = y - 4
    if y == 0:
        break
    ''''''
#contador flexible
lownum=4
highnum = 18
mult=6

for i in range(lownum,highnum+1):
    if i % mult == 0:
        print(i)

