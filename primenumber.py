def primenumber():
    A=input('Enter the number:')
    p=1
    A=int(A)
    if A>1:
        for i in range(2,A):
            if A%i == 0:
                p=0
                break
        else:
            p=1
    else:
        p=0
    return p


x=primenumber()
print(x)
