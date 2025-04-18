def times_table(start,end):
    for n in range(1, 10): 
        for i in range(start, end+1):
            print(f"{i} x {n} = {i*n:2}", end="\t")
        print()


times_table(2,5)
print()
times_table(6,9)