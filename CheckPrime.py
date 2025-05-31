def checkPrime(num):
    if num<2: return False
    if num==2: return True
    if num%2==0: return False
    for i in range(3, int(num**0.5) + 1, 2): # square root of num + 1 is the end index
        if(num%i==0): return False
    else: return True

num = int(input("Enter the Number: "))
res = bool(checkPrime(num))
if res: print(f"{num} is Prime.")
else: print(f"{num} is not Prime.")
