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
continue_bid = True
print(logo)
bid_dictionary = {}
while continue_bid:
    name = input("Enter your name?: ")
    bid_price = int(input("Enter your bid Rs. "))
    bid_dictionary[name] = bid_price

    is_Continue = input("Are there any other bidders?. Type 'Yes' or 'No' ").lower()
    if is_Continue == "no":
        continue_bid = False
winner = ""
maxi = 0
for key in bid_dictionary:
    value = bid_dictionary[key]
    if value > maxi:
        maxi = value
        winner = key
print(f"The winner of this bid is {winner} of having bid {maxi}")
