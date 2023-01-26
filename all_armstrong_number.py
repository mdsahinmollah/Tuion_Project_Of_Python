#write a program to find out the armstron number......
print("\n")

lower = int(input("Enter lower range : "))
upper = int(input("Enter upper range : "))

print("\n")

for num in range(lower,upper+1):
    i = num
    sum = 0

    while num > 0:
        rem = num % 10
        sum += rem**3
        num = num // 10
        if sum == i :
            print("All armstrong numbers are :",sum)
    
print("\n")
