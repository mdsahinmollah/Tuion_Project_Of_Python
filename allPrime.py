# Write a python program to show all prime number..

print("\n")

lower = int(input("Enter lower range : "))
upper = int(input("Enter upper range : "))
print("\n")

print(f"Prime numbers between {lower} & {upper} is : ")

for i in range(lower,upper + 1):
    if i>1:
        for num in range(2,i):
            if i%num == 0:
                break
        else:
            print("\n",i)


print("\n")