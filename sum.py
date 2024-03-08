num = input("Enter a number to find sum: ")
if num.isdigit():
    num = int(num)
    sum = 0
    for i in range(0, num+1) :
     sum += i
else :
    print("null")
break
print(sum)
