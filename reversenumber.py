rev=0
while n>0:
    a=n%10
    rev= a+10*rev
    n//=10
print(rev)
