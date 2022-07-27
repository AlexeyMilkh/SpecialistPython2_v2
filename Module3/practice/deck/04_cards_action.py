class Card:
    # TODO-0: сюда копируем реализацию класса карты из предыдущего задания
    ...


cards = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
suits = ["Hearts", "Diamonds", "Spades", "Clubs"]
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for value in values:
    for suit in suits:
        cards.append(Card(value, suit))
# TODO-2: Выведите карты в формате: cards[кол-во]2♥, 3♥, 4♥ ... A♥, 2♦, 3♦ ... A♦, ...
i = 1
for card in hearts_cards:
    cards.append(card.to_str())
    i += 1
print('cards', i, ','.join(hearts_cards_str))
