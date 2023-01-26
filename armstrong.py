# write a python script to check wheaher a number is armstrong or not?

print("\n")

n = int(input("> Enter a number :"))
arm = 0
temp = n

for i in range(1,n):
    rem = n % 10
    arm = arm + (rem**3)
    n = n // 10
if arm == temp:
    print(f'> {temp} is Armstrong number.')
else:
    print(f"> {temp} is not a armstrong number.")

print("\n")