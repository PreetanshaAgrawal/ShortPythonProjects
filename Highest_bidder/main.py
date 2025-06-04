import os, art
print(art.logo)

def highest_bidder(bid_info):
    max_bid = 0
    winner = ""
    for bidder, amount in bid_info.items():
        amount = int(amount)
        if amount > max_bid:
            max_bid = amount
            winner = bidder
    return winner, max_bid
    

def main():
    bidding = True
    bid_info = {}
    while bidding:
        bidder_name = input("Enter your name: ")
        bidder_amt = input("Enter your bid: $ ")
        next_bidder = input("Is there any other bidder? Type 'yes' or 'no': ")
        bid_info.update({bidder_name:bidder_amt})
        # print(bid_info)
        if next_bidder == 'yes':
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        else:
            winner, amount = highest_bidder(bid_info)
            bidding = False
    print(f"The winner is {winner} with a bid of ${amount}")

if __name__ == "__main__":
    main()