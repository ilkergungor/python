
#! module = a file containing python code. May contain functions, classes etc.
#!  used with modular programming which is to separate a program into parts

import messagesForModule as msg
msg.hello()
msg.bye()

from messagesForModule import hello, bye #! or import * FOR ALL 

hello()
bye()




