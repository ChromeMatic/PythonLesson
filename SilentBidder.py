from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

Bidders = {}
end_Bidding = False
result = ""


def highest_bidder(bid_record):
    highest_bid = 0
    bidder_name = ""
    for key in bid_record:
        if bid_record[key] > highest_bid:
            highest_bid = bid_record[key]
            bidder_name = key
    print(f"The winner is {bidder_name} with the amount of ${highest_bid}")


while not end_Bidding:
    print(logo)
    name = input("What's your name: ")
    bid = int(input("What's your bid : $"))

    Bidders[name] = bid

    question = input("Is their any more players ? (type yes or no) : ").lower()

    if question == "no":
        end_Bidding = True
        clear()
        highest_bidder(Bidders)
    elif question == "yes":
        clear()
