import collections

tCard = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    
    lstRank = [str(num) for num in range(2, 11)] + list('JQKA')
    lstSuit = 'spades diamonds clubs hearts'.split( )

    def __init__(self) -> None:
        self.m_cardList = [tCard(sRank, sSuit) for sSuit in self.lstSuit
                                                for sRank in self.lstRank]

    def __len__(self):
        return len(self.m_cardList)

    def __getitem__(self, iPos):
        return self.m_cardList[iPos] 

card = tCard('7','hello')
print(card)

oDeck = FrenchDeck()
print(len(oDeck))
print(oDeck[0])
print(oDeck[-1])

from random import choice
print(choice(oDeck))

print(oDeck[:3])
print(oDeck[12::13])

for idx, tCardtemp in enumerate(oDeck):
    print("index: %d, card : %s" % (idx, tCardtemp))

for idx, tCardtemp in enumerate(reversed(oDeck)):
    print("index: %d, card : %s" % (idx, tCardtemp))

# for idx, tCard in enumerate(reversed(oDeck)):
#     print("index: %d, card : %s" % (idx, tCard))
# 如果这里面循环命名 tCard 会使下面创建 card2 失败
print(card in oDeck)

card2 = tCard('7','hearts')

print(card2 in oDeck)

dSuitValues  = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def SpadesHigh(card):
    rankValue = FrenchDeck.lstRank.index(card.rank)
    return rankValue * len(dSuitValues) + dSuitValues[card.suit]

print(SpadesHigh(card2))

for card in sorted(oDeck, key=SpadesHigh):
    print(card)