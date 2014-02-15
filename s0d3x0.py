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

denom = [50,35,20,10]
rem = [s._50,s._35,s._20,s._10]

if args.bill is not None:
    f = open("dump","w")
    
    for i in range(4):
        n = args.bill/denom[i]
        if n <= rem[i]:
            print "{:^3}{:^3}{:^3}".format(n,'x',denom[i])
            f.write("{}{}".format(rem[i]-n,"\n"))
            args.bill %= denom[i]
        else:
            print "{:^3}{:^3}{:^3}".format(rem[i],'x',denom[i])
	    f.write("{}{}".format(0,"\n"))
	    args.bill -= rem[i]*denom[i]    
    
    print "Rs.{:<3} to be paid in cash.".format(args.bill)
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
