name = "Zed A. Shaw"
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
switch_inches_cm = height * 2.54
switch_lbs_kg = weight * 0.4535924

print ("Let's talk about %s" % name)
print ("He's %d inches tall" %height)
print ("He's %d cm tall" %switch_inches_cm)
print ("He's %d pounds heavy." %weight)
print ("He's %d kg heavy." %switch_lbs_kg)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." %(eyes,hair))
print ("His teeth are usually %s depending on the coffee." %teeth)
print ("If I add %d,%d,and %d I get %d." %(age,height,weight,age +height + weight))
