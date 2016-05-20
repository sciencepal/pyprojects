# text to speech converter

import pyttsx

a='y'
while (a!='n' and a!='N'):
    print "Enter string to speak"
    e=pyttsx.init()
    x=raw_input()
    #print "you entered : ",x
    e.say(x)
    e.runAndWait()
    e.stop()
    del e
    #engine=pyttsx.init()
    print 'Enter y to speak again n to stop'
    a=raw_input()