a,b,c=map(int,input().split())
if(c/2<b):
    if(a%2==0):
        print(round((a/2)*c))
        
    else:
        print(round(((a-1)/2)*c+b))
else:
    print(int(a)*int(b));
