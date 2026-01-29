num = int(input("enter a number: "))
sum = 0
temp = num
while temp > 0:
    dijit = temp % 10
    sum += dijit ** 3
    temp //=10
    if num == sum:
        print(num,"is an amstrong number")
else:
    print(num,"is not amstrong number")