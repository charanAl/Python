from calculator import square

def test_positive():
    assert square(2)==4
    assert square(3)==9

def test_negative():
    assert square(-2) ==4
    assert square(-3) ==9

def test_zero():
    assert square(0) ==0

# def test_str():
#     with pytest raise("TypeError")


    # if square(2)!=4:
    #     print("2 is square was not 4")
    # if square(3)!=9:
    #     print("3 is square was not 9")

# if __name__=="__main__":

#     main()