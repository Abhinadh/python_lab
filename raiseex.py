n=int(input("entre the integer number"))
try:
    if(n<90 or n>120):        #raise exception
        raise ValueError("Abnormal condition")
except ValueError as er:
    print(er)
else:
    print("entered value is:%d",n)
    
