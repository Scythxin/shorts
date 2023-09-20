a=[2,4,1,6,5,8]
tar=10
for i in a:
    if tar-i in a:
        print(i,",", tar-i, "=", tar)