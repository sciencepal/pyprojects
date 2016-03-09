# text to speech converter

import pyttsx

a='y'
while (a!='n' and a!='N'):
    x=""
    print "Enter string to speak"
    x=raw_input()
    engine=pyttsx.init()
    engine.say(x)
    engine.runAndWait()
    engine=pyttsx.init()
    print 'Enter y to speak again n to stop'
    a=raw_input()
