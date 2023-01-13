import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

# cara membuat kelas
class FrenchDeck:
    # list dalam bahasa c/rust/javascript adalah array
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    # function dalam python
    # self berfungsi sebagai mamanggil semua variable dalam kelas diluar scope tidak dapat mengakses variable
    # mirip seperti struct dan self dalam rust
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

# cara memanggil kelas
deck = FrenchDeck

beer_card = Card('7', 'Diamonds')
print(beer_card)

deck = FrenchDeck()
print(len(deck))

print(choice(deck))
print(deck[12::13])

# looping dalam python
for card in deck:
    print(card)

for card in reversed(deck):
    print(card)

# dict merupaakan sekumpulan data yang berisikan value dalam javascript mirip seperti object
suit_card = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_card) + suit_card[card.suit]

for card in sorted(deck, key=spades_high):
    print(card)