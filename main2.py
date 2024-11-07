#Activity2
largest=int(input("Enter largest number: "))
smallest=int(input("Enter smallest number: "))
while smallest:
    store=smallest
    smallest=largest%smallest
    largest=store
print("HCF is ",largest)