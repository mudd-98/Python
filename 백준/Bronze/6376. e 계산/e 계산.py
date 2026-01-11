import math

print("n e")
print("- -----------")

e = 0.0
for i in range(10):
    e += 1 / math.factorial(i)
    
    # n = 0, 1 (int)
    if i < 2:
        print(f"{i} {int(e)}")
    
    # n = 2 (2.5 float)
    elif i == 2:
        print(f"{i} {float(e)}")
    
    # n >= 3 (.9)
    else:
        print(f"{i} {e:.9f}")