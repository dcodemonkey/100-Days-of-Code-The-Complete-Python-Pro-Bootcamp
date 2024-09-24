from art import logo
print(logo)

def largest_bidder(biding_record):
    highest_bid = 0
    winner = ""
    for bidder in biding_record:
        bid_amount = biding_record[bidder]
        # TODO-4: Compare bids in dictionary
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

bids = {}
keep_biding = True

while keep_biding:
    # TODO-1: Ask the user for input
    name = str(input("What is your name?: "))
    price = int(input("What is your bid?: $"))
    # TODO-2: Save data into dictionary {name: price}
    bids[name] = price
    # TODO-3: Whether if new bids need to be added
    more_bidder = str(input("Are there any other bidders? Type 'yes or 'no'.")).lower()
    if more_bidder == 'yes':
        keep_biding = True
    else:
        keep_biding = False

largest_bidder(bids)






