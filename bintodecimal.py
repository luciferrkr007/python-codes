
def bintodeci(bb):
    sum=0
    for i in range(len(bb)):
        digit = bb.pop()
        digit=int(digit)
        if digit==1:
            sum=sum+pow(2,i)
    return sum



x=list(input('enter the number: '))
y=bintodeci(x)
print(y)
        
