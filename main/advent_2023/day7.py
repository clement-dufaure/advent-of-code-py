from collections import Counter

from main.utils.files_utils import lire_fichier

ordre_des_cartes = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
ordre_des_cartes_avec_joker = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]


def find_hand_with_joker(cards: str) -> int:
    jokers_count = cards.count("J")
    if jokers_count == 0:
        return find_hand(cards)
    if jokers_count == 5:
        return 7
    cards_sans_joker = cards.replace("J", "")
    effectifs = Counter(cards_sans_joker)
    effectifs_sorted = sorted(effectifs.items(), key=lambda item: item[1], reverse=True)
    return find_hand(cards.replace("J", effectifs_sorted[0][0]))


def find_hand(cards: str) -> int:
    # 1 High card 5
    # 2 One pair 4
    # 3 Two pair 3
    # 4 Three of a kind 3
    # 5 Full house 2
    # 6 Four of a kind 2
    # 7 Fifth of a kind 1
    effectifs = Counter(cards)
    # effectif : valeur => effectif
    if len(effectifs) == 5:
        # High card
        return 1
    if len(effectifs) == 4:
        # One pair
        return 2
    if len(effectifs) == 3:
        if sorted(effectifs.values(), reverse=True)[0] == 2:
            # Two Pair
            return 3
        # Three of a kind
        return 4
    if len(effectifs) == 2:
        if sorted(effectifs.values(), reverse=True)[0] == 3:
            # Full House
            return 5
        # Four of a kind
        return 6
    return 7


class CamelCardHand:
    def __init__(self, cards: str, bid: int, with_joker: bool = False):
        self.cards = cards
        self.bid = bid
        self.with_joker = with_joker
        self.hand_force = find_hand(cards) if not with_joker else find_hand_with_joker(cards)

    def __lt__(self, other):
        if self.hand_force == other.hand_force:
            if not self.with_joker:
                for i in range(len(self.cards)):
                    if self.cards[i] != other.cards[i]:
                        return ordre_des_cartes.index(self.cards[i]) < ordre_des_cartes.index(other.cards[i])
            else:
                for i in range(len(self.cards)):
                    if self.cards[i] != other.cards[i]:
                        return ordre_des_cartes_avec_joker.index(self.cards[i]) < ordre_des_cartes_avec_joker.index(
                            other.cards[i])
        return self.hand_force < other.hand_force

    def __repr__(self):
        return f"{self.cards}({self.hand_force})"


def part1(input_path):
    hands: list[CamelCardHand] = []
    for ligne in lire_fichier(input_path):
        cards, bid = ligne.split(" ")
        hands.append(CamelCardHand(cards, int(bid)))
    sorted_hands = sorted(hands)
    scores: list[int] = []
    for i, hand in enumerate(sorted_hands):
        scores.append((i + 1) * hand.bid)
    return sum(scores)


def part2(input_path):
    hands: list[CamelCardHand] = []
    for ligne in lire_fichier(input_path):
        cards, bid = ligne.split(" ")
        hands.append(CamelCardHand(cards, int(bid), True))
    sorted_hands = sorted(hands)
    scores: list[int] = []
    for i, hand in enumerate(sorted_hands):
        scores.append((i + 1) * hand.bid)
    return sum(scores)
