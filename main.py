input("Set a bit-OR turn on. Press Enter.")
print("5=",bin(5)[2:])
print("7=",bin(7)[2:])

input("Power of 2 if only 1 bit is on. Press Enter")
n=int(input("Enter a number: "))
if n>0 and n& (n-1) == 0:
    print(f"{n} is a power of 2.")
else:
    print(f"{n} is not a power of 2.")

input("First set bit is the rightmost bit that is set. Press Enter.")
print("5=",bin(5)[2:], "First set bit position is", (5 & -5).bit_length())
print("4=",bin(4)[2:], "First set bit position is", (4 & -4).bit_length())

input("Bit masking is -one 1 exactly at the position. Press Enter.")
n=int(input("Enter a number: "))
k=int(input("Enter a position: "))
for k in range(4):
    print(f"Mask for position {k} is {bin(1<<k)[2:]}")