a=10
b=0
try:
    c=a/b
except Exception as ex :
    print(ex)
finally:
    print(b/a)
