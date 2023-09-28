a,b,c=map(int,input().split())

a1=a+b+c
a2=2*a+2*b
a3=2*a+2*c
a4=2*b+2*c

print(min(a1,a2,a3,a4))
