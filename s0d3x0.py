#A coupon book contains coupons worth Rs.1000
#10 coupons of Rs.50
#8 coupons of Rs.35
#6 coupons of Rs.20
#10 coupons of Rs.10


import argparse,sys

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

parser = argparse.ArgumentParser()
parser.add_argument("--addBook",help = "Adds a CouponBook",action = "store_true")
parser.add_argument("--display",help = "Displays the remaining coupons",action = "store_true")
parser.add_argument("--bill",help = "Total bill amount",type = int)
args = parser.parse_args()


