# Write a python script to find the largest element in a list......
print("\n")                 # for space

a = []
m = 0
i = 0

n = int(input("Enter the size of the list : "))
for i in range(0,n):
    x = int(input("Enter the number : "))
    a.append(x)

for i in range(0,n):
    if a[i] > m :
        m = a[i]
        
print("\n")               # for space

print(f"{m} is largest number in this list at the index of {i}.")

print("\n")               # for space