#A coupon book contains coupons worth Rs.1000
#10 coupons of Rs.50
#8 coupons of Rs.35
#6 coupons of Rs.20
#10 coupons of Rs.10


import argparse,json,os

BOOK_FILE = "dump"



class CouponBook(object):
    def __init__(self):
        if os.path.exists(BOOK_FILE):
            f = open(BOOK_FILE,"a+")
            self.denom = json.load(f)
        else:
            self.denom = {50:0,
                          35:0,
                          20:0,
                          10:0}

    def save(self):
        f = open(BOOK_FILE,"w")
        json.dump(self.denom,f)

    def add_book(self):
        book  = {50:10,
                 35:8,
                 20:6,
                 10:10}
        for i,j in book.items():
            self.denom[i] += j
        self.save()

    def show_status(self):
        print "Coupons Remaining"
        for i,j in self.denom.items():
            print "Rs. {:^3} - {:^3}".format(i,j)

    def compute(self,amt):
        print "Coupons to be given"
        x = [int(i)   for i,j in self.denom.items()]
        x.sort(reverse=True)
        for i in x:
            n = amt/i
            if n>self.denom[str(i)]:
                amt -= i*self.denom[str(i)]
                print "{:^3} of Rs. {:^3}".format(self.denom[str(i)],i)
                self.denom[str(i)] = 0
            else:
                amt -= i*n
                self.denom[str(i)] -= n
                print "{:^3} of Rs. {:^3}".format(n,i)
        print "Remaining Rs. {:^3} to be paid in cash".format(amt)
        self.save()

def main():
    s = CouponBook()
    args = parser.parse_args()

    if args.addBook:
        s.add_book()

    elif args.display:
        s.show_status()

    elif args.bill:
        s.compute(args.bill)

    else:
        print "Bad arguments"
        

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required = True)
group.add_argument("--addBook",help = "Adds a CouponBook",action = "store_true")
group.add_argument("--display",help = "Displays the remaining coupons",action = "store_true")
group.add_argument("bill",nargs = '?',help = "Total bill amount",type = int)


main()
