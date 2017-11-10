from sys import argv
script, fileName  = argv
print ("We're going to erase %r." %fileName)
print ("If you don't want that ,hit CTRL+C(^C).")
print ("If you do want that,hit RETURN.")

input("?")

print ("Openning the file...")
target = open(fileName,'w')

print ("Truncate the file.Goodbye!")
target.truncate()

print ("Now I'm going to ask you for three lines.")

line1 = input("line 1:")
line2 = input("line 2:")
line3 = input("line 3:")


#1
target.write("%s\n%s\n%s\n"%(line1,line2,line3))

#2
target.write("""
%r
%r
%r\n"""%(line1,line2,line3))

#3
target.write(line1)

print ("And finally,we close it")
target.close()
