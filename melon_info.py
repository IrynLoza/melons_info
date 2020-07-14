"""Print out all the melons in our inventory."""


from melons import melon_names, melon_seedlessness, melon_prices
from collections import defaultdict

def print_melon(name, seedless, price):
    """Print each melon with corresponding attribute information."""

    have_or_have_not = True
    if seedless:
        have_or_have_not = False

    #print(f'{name}s {have_or_have_not} seeds and are ${price:.2f}')
    #melons = defaultdict(lambda: None)
    melons = { 
        melon_names[i]: {
        "seedless": have_or_have_not,
        'price': melon_prices[i],
        'flesh_color': None,
        'weight': None,
        'rind_color': None
        }
    }

    for (key, value) in melons.items():
        print(f'{key} {value}')


for i in melon_names:
    print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
