'''
n=int(input('input your no: '))
for i in range(1,n+1):
    if n%2!=0:
        if i%2!=0:
            s=str(int((n-i)/2)*' ')
            print(s+(i*'*')+s)

for i in ((n+2)*'e'):
    if n>0:
        sp=int((n-len(i))/2)*' '
        print(sp+i+sp)

for i in range(n+2):
    print((n)*'*')


print('-------------------------------------------')
'''
'''

for i in range(1,6):
    if i==1:
        print(i*'*')
    elif i==2:
        s=i*'* '
        l1=s.split(' ')
        l1.remove('')
        l1[0]='+'
        for i in l1:
            print(i,end='')
        print(' ')
    elif i==3:
        s=i*'+ '
        l2=s.split(' ')
        l2.remove('')
        l2[1]='*'
        for i in l2:
            print(i,end='')
        print(' ')
    elif i==4:
        s=i*'* '
        l3=s.split(' ')
        l3.remove('')
        l3[1]='+'
        l3[3]='+' 
        for i in l3:
            print(i,end='')
        print(' ')
    else:
        s=i*'+ '
        l4=s.split(' ')
        l4.remove('')
        l4[1]='*'
        l4[3]='*'  
        for i in l4:
            print(i,end='')
        print(' ')
print("------------------------------------------------------------------")

'''

'''
n=int(input('please enter any no: '))
sum=0
temp=n

for digit in str(n):
    sum += int(digit)**3


if(sum==temp):
    print(f'{temp} is an Armstrong no')
else:
    print(f'{temp} is not an Armstrong no')



print("------------------------------------------------------------------")
'''
'''
n=int(input('please enter any no: '))
sum=0
sum1=0

for i in str(digit):
    if int(i)%2==0:
        sum+=i**2
        print('sum of square of even no',sum)
    elif int(i)%2!=0:
        sum1=sum1+int(i)**3
        print('sum of qube of odd no',sum1)
    else:
        pass


print("------------------------------------------------------------------")
'''


my_dict = {"a": 1, "b": 2, "c": 3}

for k, v in my_dict.items():
    print(k,'is', v)




print('---------------------------------------------------')

list = [1, 2, 3,4,5,6,7,8]

list1 = ['#' if i%2==0 else i for i in list]

print(list1)  

print('---------------------------------------------------')


lst = [[1,2,3,],[4,5,6]]

for a,*b in lst:
    print('value of b=',b)


for a,*b in lst:
    print('value of a=',a)
















































         

        
        
            
        
    
        