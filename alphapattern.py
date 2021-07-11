N=int(input())
i=1
while i<=N:
    j=1

    while j<=i:
        print(chr(64+i),end="")
        j=j+1

    print()
    i=i+1
