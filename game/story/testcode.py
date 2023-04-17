import random

from game.model.card import Card


def roulette_wheel_selection(cards):
    non_int_values = [card for card in cards if not isinstance(card.value, int)]
    int_values = [card for card in cards if isinstance(card.value, int)]

    total_weight = sum([len(non_int_values) * 1.5, len(int_values)])

    pick = random.uniform(0, total_weight)

    if pick < len(int_values):
        return random.choice(int_values)
    else:
        return random.choice(non_int_values)

if __name__ == '__main__':
    cards = [Card('red', 1), Card('blue', 'skill1'), Card('green', 2), Card('yellow', 'skill2'), Card('white', 'skill3'), Card('black', 5)]

    skill_cnt = 0
    num_cnt = 0
    for i in range(1000):
        if not isinstance(roulette_wheel_selection(cards).value, int):
            skill_cnt += 1
        else:
            num_cnt += 1

    skill_ratio = skill_cnt / 1000
    print(skill_ratio)
    error = abs(skill_ratio - 0.6) / 0.6
    print(f'오차: {error}')
    print(f'테스트 통과 여부: {error <= 0.05}')

    print(skill_cnt, num_cnt)