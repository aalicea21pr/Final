def credit_card_penalty(balance,number):
    if number < 15:
        return balance * 0.05
    elif number >= 15 and number <= 30:
        return balance * 0.10
    elif number >= 31 and number <= 60:
        return balance * 0.15
    else:
        return balance * 0.20

print "penalty 1:", credit_card_penalty(15000,18)
print "penalty 2:", credit_card_penalty(7000,31)
print "penalty 3:", credit_card_penalty(300,70)
print "penalty 4:", credit_card_penalty(1000,3)
