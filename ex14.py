from sys import argv

script  ,sex= argv
prompt = '>'

print ("What's your name ?")
user_name = input(prompt) 
 
print ("Hi %s,I'm the %s scrpit." %(user_name,script))
print ("Do you like me %s?"%user_name)
likes = input(prompt)

print ("Do you live %s?"%user_name)
lives = input(prompt)

print ("What kind of computer do you have?")
computer = input(prompt)


print ('''
Alright,so you said %r about liking me.
You live in %r.
You are %r.
''' %(likes,lives,sex))
