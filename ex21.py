def add(a,b):
    print ("ADDING %d + %d" %(a,b))
    return a+b

def subtract(a,b):
    print ("SUBTRACTING %d -%d" %(a,b))
    return a-b

def multiply(a,b):
    print ("MULTIPLY %d * %d" %(a,b))
    return a *b

def divide(a,b):
    print ("DIVIDE %d / %d" %(a,b))
    return a/b


age =add(20,8)
height = subtract(180,7)
weight = multiply(90,2)
iq = divide (300,2)

print("Age:%d,Height：%d,Weight: %d,IQ: %d"%(age,height,weight,iq))

what = add(age,subtract(height,multiply(weight,divide(iq,2))))

print (what)


number_divide = divide(iq,2)
number_multiply = multiply(weight,number_divide)
number_subract = subtract(height,number_multiply)
what = add(age,number_subract)
print (what)
