#A coupon book contains coupons worth Rs.1000
#10 coupons of Rs.50
#8 coupons of Rs.35
#6 coupons of Rs.20
#10 coupons of Rs.10


import argparse,json,os

BOOK_FILE = "dump"



class CouponBook(object):
    def __init__(self, book_file):
        self.denom = {50:0,
                      35:0,
                      20:0,
                      10:0}
        if os.path.exists(book_file):
            self.load(book_file)

    def save(self, book_file):
        f = open(book_file,"w")
        json.dump(self.denom,f)

    def load(self, book_file):
        f = open(book_file, "r")
        self.denom = json.load(f)

    def add_book(self):
        book  = {50:10,
                 35:8,
                 20:6,
                 10:10}
        for i,j in book.items():
            self.denom[i] += j

    def show_status(self):
        print "Coupons Remaining"
        for i,j in self.denom.items():
            print "Rs. {:^3} - {:^3}".format(i,j)

    def compute(self,amt):
        print "Coupons to be given"
        x = self.denom.keys()
        x.sort(reverse=True)
        for i in x:
            n = amt/i
            if n>self.denom[i]:
                amt -= i*self.denom[i]
                print "{:^3} of Rs. {:^3}".format(self.denom[i],i)
                self.denom[i] = 0
            else:
                amt -= i*n
                self.denom[i] -= n
                print "{:^3} of Rs. {:^3}".format(n,i)
        print "Remaining Rs. {:^3} to be paid in cash".format(amt)

def parse_args():
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required = True)
    group.add_argument("--addBook",help = "Adds a CouponBook",action = "store_true")
    group.add_argument("--display",help = "Displays the remaining coupons",action = "store_true")
    group.add_argument("bill",nargs = '?',help = "Total bill amount",type = int)
    args = parser.parse_args()
    return args

def main():
    s = CouponBook(BOOK_FILE)
    args = parse_args()

    if args.addBook:
        s.add_book()

    elif args.display:
        s.show_status()

    elif args.bill:
        s.compute(args.bill)

    else:
        print "Bad arguments"
    s.save(BOOK_FILE)



main()
