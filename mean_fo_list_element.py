# Write a python script to find mean of the list element......
print("\n")

a = []
sum = 0
mean = 0

n = int(input("Enter the size of the list : "))
for i in range(0,n):
    x = int(input("Enter the number : "))
    a.append(x)

for i in range(0,n):
    sum = sum + a[i]


mean = sum / n

print("Mean is : ",mean)

print("\n")