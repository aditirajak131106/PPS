a = list(map(int,input("Set A: ").split()))
A = set(a)
b = list(map(int,input("Set B: ").split()))
B = set(b)
print(f"Union:  {A|B}")
print(f"Intersection:  {A&B}")
print(f"Difference:  {A-B}")
# Write your code here to perform different operations
