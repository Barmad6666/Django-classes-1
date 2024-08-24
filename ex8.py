def hi():
    print("01",end="")
    try :
        hi()
    except:
        hi()
hi()