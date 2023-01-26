# Write a python program to check wheather a number is prime or not?

print("\n")

n = int(input("Enter a number : "))

flag = 0
if n > 1:
    for i in range(2,n):
        if n % i == 0:
            flag = 1
            break

if flag == 0:
    print(f"{n} is prime number.")

else:
    print(f"{n} is not prime.")

print("\n")
