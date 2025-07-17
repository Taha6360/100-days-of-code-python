import  art
print(art.logo)
bid={}
def func():
    name = input("Enter your name")
    each_bid = int(input("Enter your bid"))
    bid[name] = each_bid
    continue_or_not = input("If there are another person to bid yes or no? ").lower()
    maxi=0
    winer = ""
    if continue_or_not == "yes":
        print ("\n" * 20)
        func()
    else:
        highest_amount = 0
        for items in bid:
            bid_amount = bid[items]
            if bid_amount> highest_amount:
                highest_amount = bid_amount
                winer = items
        print( f"\n the highest bid was {maxi}  placed by {winer}")

func()

