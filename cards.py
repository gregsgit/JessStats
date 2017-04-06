#!/usr/bin/env python3

import sys
from math import factorial as fact

# n choose k = [ n (n - 1) (n - 2) ... (n - k + 1) ] / [ k (k - 1) ... 1]
def n_choose_k(n, k):
    numerator = n
    for i in range(n - 1, n - k, -1):
        numerator = numerator * i

    denominator = k
    for i in range(k - 1, 0, -1):
        denominator = denominator * i

    return numerator / denominator

num_5_card_hands = n_choose_k(52, 5)

# full house: chances of getting dealt full house (3-of-a-kind and a pair).

# From: Andre' Nicolas
# (http://math.stackexchange.com/users/6312/andr%c3%a9-nicolas), How
# to calculate a fullhouse after dealing 5 cards?, URL (version:
# 2012-09-08): http://math.stackexchange.com/q/192794

# There are 13-choose-1 ways to ways to choose the kind we have three
# of. For each of these ways, the actual cards can be chosen in
# 4-choose-3 ways. For each way of getting so far, there are
# 12-choose-1 ways to choose the kind we have two of, and for each
# there are 4-choose-2 ways to choose the actual cards. So our
# probability is:
#   (13-choose-1 * 4-choose-3 * 12-choose-1 * 4-choose-2) / 52-choose-5
def full_house():
    num = n_choose_k(13, 1) * n_choose_k(4, 3) * n_choose_k(12, 1) * n_choose_k(4, 2)
    return num / num_5_card_hands

# there are exactly 4 different royal flush hands (one for each suit)
def royal_flush():
    return 4 / num_5_card_hands

# calculate n choose k the "simpler" but slower way:
#   = n! / (k! * (n-k)!)
def n_choose_k_the_slow_way(n, k):
    if k < 0 or k > n:
        print("k ({}) must be between 0 and n ({})".format(k, n, file=sys.stderr))
        sys.exit()

    fact_n = fact(n)
    fact_k = fact(k)
    fact_n_minus_k = fact(n - k)
    return fact_n / (fact_k * fact_n_minus_k)

if __name__ == "__main__":
    print("total number of different 5-card hands from a 52 card deck: {}.".format(num_5_card_hands))
    print("probability of full house: {}.".format(full_house()))
    print("probability of royal flush: {}.".format(royal_flush()))
