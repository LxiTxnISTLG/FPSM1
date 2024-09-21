a = 10  

def MyFunc1():  
    a = 20
    print("1:", a)

def MyFunc2():  
    print("2:", a)
    
    def SubFunc1(st):  
        print("Local Function with", st)

    SubFunc1("Local Call")  

MyFunc1()  
MyFunc2()  
