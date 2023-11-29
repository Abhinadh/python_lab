try:
    n=int(input("entre a value"))
    assert(n>0), "negative number"
except AssertionError as a:
    print(a)
print(n)

    


