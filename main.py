import art
print(art.logo)
event = True
dic = {}
while event:
    name = input("What is your name? ")
    bid = int(input("What is your bid? "))
    dic[name] = bid
    true_or_not = input("Would you like to play again? (y/n) ")
    if true_or_not == "y":
        print("\n" * 20)
    else:
        event = False
top_bid = 0
key_value = ""
for key in dic:
    if dic[key] > top_bid:
        top_bid = dic[key]
        key_value = key
print(f"The top bid is by {key_value} for {top_bid}.")
