from __future__ import print_function
import socket

#Convert a number in one base to another base, I don't have the source but this is not my code
def int2base(a, base, numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
     baseit = lambda a=a, b=base: (not a) and numerals[0]  or baseit(a-a%b,b*base)+numerals[a%b%(base-1) or (a%b) and (base-1)]
     return baseit()
     
def base2base(base, num, target):
    return int2base(int(str(num), base), target)


#Will receive one character at a time until a certain letter is hit
def stripTill(char):
    inChar = ''
    while 1: #Scan/input base
        strip = sock.recv(1)
        print(strip, end='')
        if strip == char:
            return

#Sample input from using NetCat:
# Base: [2] Num: (1011110101010) Target Base: {10}
# print(base2base(2, 1011110101010, 10))

#Open 'er up!
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Coinslot hosted on: hn.csaw.io 9002
sock.connect(("hn.csaw.io",9002))

#Keep all our code in here so we can close the connection when we're done
try:
    #Start getting data
    while 1:
		#Get the base that the given number is in
        stripTill("[")
        char = ''
        base = ''
        while not char == "]": #Scan/input base
            base += char
            char = sock.recv(1)
        sock.recv(1)
        print(base + ']')
        base = int(base)
        
        #Get the number they want us to convert
        stripTill('(')
        char = ''
        num = ''
        while not char == ")": #Scan/input base
            num += char
            char = sock.recv(1)
        sock.recv(1)
        print(num + ')')
        num = num
        
        #Find out base they want us to convert to        
        stripTill('{')
        char = ''
        target = ''
        while not char == "}": #Scan/input base
            target += char
            char = sock.recv(1)
        sock.recv(1)
        print(target + '}')
        target = int(target)
        
        #Clear buffer
        stripTill(":")
        stripTill(" ")
        
        #Print to user, convert and send number
        print(str(base2base(base, num, target)))
        sock.send(str(base2base(base, num, target))+'\n')
        
        #Have we gotten the key yet?
        if(sock.recv(3)=="key"):
            print(sock.recv(1024))
        
    
        
finally:
    ##Now Get key!!
    print(sock.recv(1024))
    
    print("")
    print ("Throwing sock away.")
    sock.close()
