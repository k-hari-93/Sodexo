#A coupon book contains coupons worth Rs.1000
#10 coupons of Rs.50
#8 coupons of Rs.35
#6 coupons of Rs.20
#10 coupons of Rs.10


import argparse

class S0d3x0(object):
    def __init__(self):
        f = open("dump","a+")
        if not f.read() == '':
            f.seek(0)
            self._50 = int(f.readline()[:-1])
            self._35 = int(f.readline()[:-1])
            self._20 = int(f.readline()[:-1])
            self._10 = int(f.readline()[:-1])
            f.close()

        else:
            self._50 = 0
            self._35 = 0
            self._20 = 0
            self._10 = 0

s = S0d3x0()
print "\n"

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument("--addBook",help = "Adds a CouponBook",action = "store_true")
group.add_argument("--display",help = "Displays the remaining coupons",action = "store_true")
group.add_argument("bill",nargs = '?',help = "Total bill amount",type = int)
args = parser.parse_args()

if args.bill is not None:
    f = open("dump","w")

    n = args.bill/50
    if n <= s._50:
        print "{:^3}{:^3}{:^3}".format(n,'x',"50")
        f.write("{}{}".format(s._50-n,"\n"))
        args.bill %= 50
    else:
        print "{:^3}{:^3}{:^3}".format(s._50,'x',"50")
	f.write("{}{}".format(0,"\n"))
	args.bill -= s._50*50

    n = args.bill/35
    if n <= s._35:
        print "{:^3}{:^3}{:^3}".format(n,'x',"35")
        f.write("{}{}".format(s._35-n,"\n"))
	args.bill %= 35
    else:
	print "{:^3}{:^3}{:^3}".format(s._35,'x',"35")
	f.write("{}{}".format(0,"\n"))
	args.bill -= s._35*35

    n = args.bill/20
    if n <= s._20:
        print "{:^3}{:^3}{:^3}".format(n,'x',"20")
        f.write("{}{}".format(s._20-n,"\n"))
	args.bill %= 20
    else:
	print "{:^3}{:^3}{:^3}".format(s._20,'x',"20")
	f.write("{}{}".format(0,"\n"))
	args.bill -= s._20*20

    n = args.bill/10
    if n <= s._10:
        print "{:^3}{:^3}{:^3}".format(n,'x',"10")
        f.write("{}{}".format(s._10-n,"\n"))
	args.bill %= 10
    else:
	print "{:^3}{:^3}{:^3}".format(s._10,'x',"10")
	f.write("{}{}".format(0,"\n"))
	args.bill -= s._10*10

    print "Rs.{:<5} to be paid in cash.".format(args.bill)
    f.close()

elif args.addBook is True:
    f = open("dump","w")
    s._50 += 10
    s._35 += 8
    s._20 += 6
    s._10 += 10
    for i in [s._50,s._35,s._20,s._10]:
        f.write("{}{}".format(i,"\n"))

    print '1 CouponBook added'
    f.close()


else:
    print "Number of coupons remaining : "
    print "{:^15}{:^15}{:^15}{:^15}".format("Fifty","Thirty-five","Twenty","Ten")
    print "{:^15}{:^15}{:^15}{:^15}".format(s._50,s._35,s._20,s._10)
        
print "\n"
