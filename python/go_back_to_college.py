# root-me 'Go back to college' Python script
import math, socket, time

# connect python to the root-me irc channel
network = 'irc.root-me.org'
port = 6667
channel = "#root-me"
name = "moosebot"
botnick = "mooseboot"
irc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

irc.connect((network,port))
irc.send('NICK mooseboot')
irc.send('USER moosebot moosebot moosebotrn')
time.sleep(3)
irc.send('JOIN #root-mern')
time.sleep(3)
irc.send('PRIVMSG cdb-moose:testrn')
time.sleep(3)
#irc.send('PART #root-mern')
#irc.send('QUITrn')
#irc.close()

# challenge mathematical process

number_1 = input("Enter number 1: ")
number_2 = input("Enter number 2: ")

def square_root_number_1(x):
    return(math.sqrt(x))
one_square = square_root_number_1(number_1)

print "The square root of Number 1 is ", one_square

multiply_by_two = one_square * number_2
print "The square root of Number 1 multiplied by Number 2 is ", multiply_by_two
rounded = str(round(multiply_by_two, 2))
print "Rounded to two decimals is: ", rounded
print " "
print "The final answer is: !ep1 -rep", rounded
