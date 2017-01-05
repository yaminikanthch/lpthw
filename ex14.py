from sys import argv

script,	user_name, = argv
#prompt = '> '

print "Hi %s, i am the %s script" %(user_name,script)
print " i would like to ask few questions"
print " Do you like me %s" % user_name
likes = raw_input()

print " %s How was your day?" % user_name
day = raw_input()

print "what is the time now %s" % user_name
time = raw_input()

