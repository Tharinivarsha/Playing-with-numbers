#Activity1
num=int(input("Enter a number: "))
original=num
reversed=0
while num>0:
    digit=num%10
    reversed=reversed*10+digit
    num//=10
if original==reversed:
    print(f"{original} is a palindrome")
else:
    print(f"{original} is a not a palindrome")