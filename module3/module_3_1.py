calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string: str):
    count_calls()

    return len(string), string.upper(), string.lower()


def is_contains(string: str, list_to_search: list):
    count_calls()

    list_to_search = [item.lower() for item in list_to_search]

    return string.lower() in list_to_search


print(string_info('I\'m Still Standing'))
print(string_info('Big in Japan'))
print(string_info('ХОЧЕШЬ?'))
print(string_info('НЕ ОТПУСКАЙ'))

print(
    is_contains(
        'Running In The Night',
        [
            'Running in the Night',
            'Never Stop',
            'Arcade Summer',
            'Wild Ones',
            'Goodbye',
            'Let\'s Talk',
            'Everything',
            'Don\'t want to Change Your Mind',
            'Bend & Break',
            'Tears',
        ],
    )
)

print(
    is_contains(
        'I Know',
        [
            'Every You Every Me',
            'The Bitter End',
            'Running Up That Hill',
            'Pure Morning',
            'Special Needs',
            'This Picture',
            'Song to Say Goodbye',
            'Beautiful James',
            'Special K',
            'Meds',
        ],
    )
)

print(
    is_contains(
        'Это пройдет',
        [
            'Я так соскучился',
            'В диапазоне',
            'Это пройдёт',
            'Я так боюсь',
            'Кто все эти люди?',
            'Россия для грустных',
            'Прости. Прощай. Привет',
            'Уроки любви',
            'Чужое горе',
            'Выйди из комнаты',
        ],
    )
)

print(
    is_contains(
        'The Equaliser (not alone)',
        [
            'Los Angeles',
            'Sunset',
            'Jason',
            'Days of Thunder',
            'Deep Blue',
            'Vampires',
            'Silence (feat. The Midnight)',
            'The Equaliser (Not Alone)',
            'River of Darkness',
            'Lost Boy',
        ],
    )
)

print(calls)
