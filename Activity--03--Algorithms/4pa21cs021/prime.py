
def isPrime(n):
    for i in range(2,int(n/2)):
        if n%i ==0:
            return False
        
        return True


num=int(input('Enter a number to determine the primality'))
if isPrime(num):
    print(num," is a prime number")
else:
    print(num," is not a prime number")