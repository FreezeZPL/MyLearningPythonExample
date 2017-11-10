formatter = "%r %r %r %r"

print (formatter%(1,2,3,4))
print (formatter%("one","two","three","four"))
print (formatter%(True,False,False,True))
print (formatter%(formatter,formatter,formatter,formatter))

# 如果字符串中含有 '  , 则输出字符串为双引号 ， 如果不包含 ' ,则输出字符串为单引号 
print (formatter%( "I had this thing.","That you could type up right.","But it didn't sing.","So I said goodnight"))
