
def baseconverter(num):
    if num>=1:
        baseconverter(num//(base))
        print(num%(base),end='')

base=int(input('Enter the base you wanna create in: '))
x=int(input('enter the number: '))
y=baseconverter(x)
print()

        
