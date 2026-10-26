for i in range(9):
    for j in range(i+1):
        if j==i:
            print(f"{i+1}*{j+1}={(i+1)*(j+1)}")
        else:
            print(f"{i+1}*{j+1}={(i+1)*(j+1)}",end="\t")
