content = {
    'start': {
        'text': 'Вы попали в подземелье. Приключения это всегда интересно, но выбраться на свободу гораздо интереснее. Давайте займемся поиском выхода! Перед вами две комнаты (слева и справа) и длинный коридор (прямо). Куда хотите пойти?',
        'buttons': ['Налево', 'Направо', 'Прямо'],
        'result': -1,
        'img': '0.jpg'
    },
    'Налево': {
        'text': '''В комнате какой-то рыцарь, да еще и с компьютером! Настоящий программист!
Ой, он кажется живой. Так-так, без паники, он пока не настроен вас убить. Но кажется, у него проблемы с кодом. Рыцарь просит вас помочь. Согласитесь?''',
        'buttons': ['Конечно помогу!', 'Нет, мне нужно найти выход.'],
        'result': -1,
        'img': '1.jpg'
    },
    'Конечно помогу!': {
        'text': 'Рыцарь оочень вами доволен! Но... настолько доволен, что решил взять вас к себе в команду... навсегда. Отныне вы заперты в серверной подземелья. Тут даже не кормят! В таких условиях вы погибли. Игра завершена.',
        'buttons': [],
        'result': 0,
        'img': '1_1.jpg'
    },
    'Нет, мне нужно найти выход.': {
        'text': 'Что ж, это было плохим решением. Рыцарь очень рассердился и запер вас в подвале. Сыро, холодно, голодно... Вы погибли. Игра завершена.',
        'buttons': [],
        'result': 0,
        'img': '1_2.jpg'
    },
    'Направо': {
        'text': '''В комнате гном. И, кажется, он совсем недружелюбен. А еще, кажется, что он уснул... Стоя!
А что, если он знает где находится выход? Вот же сложный выбор: попробовать тихо прокрасться мимо гнома и самостоятельно найти выход, или разбудить его и спросить. А что вы выберете?''',
        'buttons': ['Буду искать выход', 'Разбудить гнома'],
        'result': -1,
        'img': '2.jpg'
    },
    'Буду искать выход': {
        'text': 'Скрытность ваше второе имя! Вы очень тихо пробрались мимо гнома, а за ним была... дверь, за которой вы нашли выход из подземелья! Поздравляем, вы выиграли!',
        'buttons': [],
        'result': 1,
        'img': '2_1.jpg'
    },
    'Разбудить гнома': {
        'text': 'Это было явно плохой идеей... Во сне гном придумывал новое зелье, но вы прервали его. Он стал вне себя от злости! И состав нового зелья сразу проявился у него в голове, в котором главный ингредиент - вы... Игра завершена.',
        'buttons': [],
        'result': 0,
        'img': '2_2.jpg'
    },
    'Прямо': {
        'text': 'Вот это красота! Очень красивый зал, а в самой середине - артефакт. А может перед тем, как выбраться, захватим блестящую штучку? Как поступите?',
        'buttons': ['Искать выход', 'Взять артефакт'],
        'result': -1,
        'img': '3.jpg'
    },
    'Искать выход': {
        'text': 'Правильно! Нам чужого не надо. Через 10 минут поиска вы наткнулись на коридор, который вел... на выход! Вы выиграли. Игра завершена.',
        'buttons': [],
        'result': 1,
        'img': '3_1.jpg'
    },
    'Взять артефакт': {
        'text': 'Это было плохой идеей. Тут же в комнате появился хранитель подземелья. Вы не в состоянии противостоять ему. Игра завершена.',
        'buttons': [],
        'result': 0,
        'img': '3_2.jpg'
    }
}