altura =10
espacios= altura
carac=1

for i in range(altura):
    for j in range(espacios):
        print("  ",end="")
    for k in range((i*2+1)):
            print("* ",end="")
           
    espacios-=1
    print()
