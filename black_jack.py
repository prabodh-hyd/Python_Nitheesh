"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    if card in ['J', 'Q', 'K']:
        return 10
    elif card == 'A':
        return 1
    else:
        return int(card)



def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one:
    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)
    if value_one > value_two:
        return card_one
    elif value_two > value_one:
        return card_two
    else:
        return card_one, card_two

def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one:
    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """
    value_one = 0
    value_two = 0
    if card_one == "A":
        value_one = ace_value(card_one, card_two)
    elif card_two == "A":
        value_two = ace_value(card_one, card_two)
    else:
        value_one = value_of_card(card_one)
        value_two = value_of_card(card_two)

    current_value = value_one + value_two
    if (current_value + 11) <= 21:
        return 11
    else:
        return 1




def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one:
    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    ten_cards = ['10','J', 'Q', 'K']

    return ('A' in [card_one, card_two]) and ((card_one in ten_cards) or (card_two in ten_cards))







def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one:
    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    return value_of_card(card_one) == value_of_card(card_two)




def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one:
    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    cards_sum = value_of_card(card_one) + value_of_card(card_two)
    return cards_sum in [9,10,11]

def ace_value(one, two):
    if one == "A":
        two_card = value_of_card(two)
        if 11 + two_card <=21:
            return 11
        else:
            return 1
    elif two == "A":
        one_card = value_of_card(one)
        if 11 + one_card <=21:
            return 11
        else:
            return 1
