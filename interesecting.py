n=int(input())
i=1
while i<=n:
    j=1
    startchar=chr(ord('A')+n-i)
    while j<=i:
        char=chr(ord(startchar)+j-1)
        print(char,end='')
        j=j+1
    print()
    i=i+1
        
