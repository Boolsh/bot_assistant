# bot.py
import os
from sys import exit
import random

import discord
from dotenv import load_dotenv

import nltk

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
if not TOKEN:
    exit('TOKEN = None')

client = discord.Client()


def is_similar_to(text1, text2):  # Похожая на ...
    # Добрый вечер
    # Дбрый вечер
    # Добрый вече

    # Добрый вечер

    # Добрый дечер
    # Добрый денер
    # Добрый деньр
    # Добрый день

    # Добрый день

    # Расстояние = 4
    # Изменение в проценнтах = 4/26 (= 0.15) Какой хороший Добрый день
    # Изменение в проценнтах = 4/26 (= 0.33) Добрый день
    distance = nltk.edit_distance(text1, text2)
    difference = distance / len(text1)
    print(distance, difference)

    if difference < 0.35:
        return True
    return False


@client.event
async def on_ready():
    print(f'{client.user.name} подключился к Discord!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, Приветствуем тебя на нашем сервере!'
    )

    response = start_dialogue(message.content)
    await message.channel.send(response)


def clear_phrases(replica):
    replica = replica.lower()
    alfabet_russ = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alfabet_engl = 'abcdefghijklmnopqrstuvwxyz'
    some_symbols = ' -'

    replica_copy = ''
    for symbol in replica:
        if symbol in (alfabet_russ + alfabet_engl + some_symbols):
            replica_copy += symbol  # replica_copy = replica_copy + symbol

    replica = replica_copy
    return replica


def get_intent(replica):
    # for items in BOT_CONFIG.items():
    #     print(items)

    # print(replica)

    for example in hello_examples:
        if is_similar_to(replica, example.lower()):
            return 'hello'

    for example in goodbye_examples:
        if is_similar_to(replica, example.lower()):
            return 'goodbye'

    for example in what_gift_do_you_want_examples:
        if is_similar_to(replica, example.lower()):
            return 'what_gift_do_you_want'

    for example in music_examples:
        if is_similar_to(replica, example.lower()):
            return 'music'

    return None


def start_dialogue(replica):
    # NLU (Natural Language Understanding):
    #  Предварительная обработка реплики (очистка, регистр букв и т.п.)
    #  Относим реплику к какому-либо классу намерений
    #  Извлекаем параметры реплики (извлечение сущностей и объектов)

    # NLG (Natural Language Generation):
    #  Выдать заготовленный ответ основываясь на намерении
    #  Если заготовленного ответа нет, то сгенерировать ответ автоматически и выдать его
    #  Если не удалось сгенерировать ответ, то выдать фразу: "Я непонял"; "Перефразируй" и т.п.

    # NLU (Natural Language Understanding):
    #  Предварительная обработка реплики (очистка, регистр букв и т.п.)
    replica = clear_phrases(replica)
    answer = replica
    return answer

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if is_similar_to(message.content.lower(), "что ты умеешь?"):
        quotes = [
            'Пока что ничего.',
            'Ничего!',
            '... ничего. Научи меня.'
        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    elif is_similar_to(message.content.lower(),'копия с гитхаб'):
        quotes = [
            'не нужна тебе копия, иди маме помоги лучше'

        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    elif '!' in message.content:
        text1, text2 = message.content.split(',')
        print(text1[1:], text2)

        if is_similar_to(text1[1:], text2):
            response = 'Фразы похожи'
        else:
            response = 'Фразы Не похожи'

        #await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException

    if is_similar_to(message.content.lower(), "привет"):
        quotes = [
            'шалом',
            'вечер в хату',
            'Ас-саляму алейкум',
            "ساعدني ، أنا محتجز كرهينة"

        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    if is_similar_to(message.content.lower(), "пока"):
        quotes = [
            'удачи',
            'прощай, ♂Dungeon Master♂',
            'бб',

        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    if is_similar_to(message.content.lower(), "кто ты?"):
        quotes = [
            'президент украины'

        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    if is_similar_to(message.content.lower(), "кто такая мортра?"):
        quotes = [
            'фантомка'

        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    if is_similar_to(message.content.lower(), "бб"):
        quotes = [
            'удачи',
            'прощай, ♂Dungeon Master♂',
            'бб',

        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    if is_similar_to(message.content.lower(), "шо ты за сало?"):
        quotes = [
            'сам ты сало',



        ]
        response = random.choice(quotes)
        await message.channel.send(response)
    if is_similar_to(message.content.lower(), "какашка"):
            quotes = [
                ':poop:'

            ]
            response = random.choice(quotes)
            await message.channel.send(response)
    '''if is_similar_to(message.content.lower(), "анекдот"):
            quotes = [
                'В афганском селе идёт по улице мужик, а впереди него жена. Навстречу им идёт старик и говорит:'
                '-Эй, Абдул, ты что Коран не читал? Жена должна идти позади мужа всегда!'
                'Мужик в ответ старику говорит:'
                '-Послушай, старый, когда Коран писали, дороги ещё не минировали.'
                'Вперёд, Фатима!',
                "Два брата грузина купили себе по лошади. Катались до вечера. Загнали в конюшню и говорят:"
                "- Как мы их различать будем?- Давай я своему ухо отрежу. У меня будет конь с одним ухом, а у тебя с двумя."
                "- Хорошо."
                "Подслушивал их сосед и завидовал. Запрыгнул в конюшню и отрезал ухо. "
                "На следующий день братья приходят и видят двух коней без одного уха. Покатались и говорят:"
                "- Как их теперь различать будем?"
                "- Давай я своему ухо отрежу. Будет у тебя конь с одним ухом, а у меня конь без ушей."
                "- Хорошо."
                "Подслушивал их сосед. Запрыгнул в конюшню и отрезал ухо. На следующий день братья приходят и видят двух коней без ушей. Покатались и говорят:"
                "- Как их теперь различать будем?- Давай я своему хвост отрешу. У будет конь без ушей с хвостом, а у меня без ушей без хвоста."
                "- Хорошо."
                "Подслушивал их сосед. Запрыгнул в конюшню и отрезал хвост коню. "
                "На следующий день братья приходят и видят двух коней без ушей и без хвостов. Говорят:"
                "- Как мы их теперь различать будем?- Давай твой тот чёрный , а мой белый.",
                "Мальчик нашел консервную банку, подходит к милиционеру:"
                "- Дяденька, откройте, пожалуйста!Милиционер стучит в банку:"
                "- Откройте, милиция!",
                "С небоскреба одновременно падают негр и цыган. Кто упадет первым?"
                "."
                "."
                "Уровень преступности",
                "— Джо, с этой сигарой вы смахиваете на пидараса."
                "— Прошу прощения, Бил, я буду смахивать в другую сторону",
                "- Папа, что такое некомпетентность и безразличие?"
                "- не знаю, сынок, не разбираюсь я в этом, да и оно мне собственно до пизды",
                "Пацаны покупают сигареты возле ларька, один купил пачку, смотрит на неё и говорит:"
                "у меня рак, а у тебя че? "
                " а у меня импотенция"
                "А че грустный такой?"
                "А я не курю просто",
                "Купили дед с бабкой приемник, воткнули в розетку на 220. Тишина, дымок пошел..."
                "– Дед, а чегой-то они там молчат?"
                "– Вот сейчас покурят, потом, глядишь, чего и скажут...",


            ]
            response = random.choice(quotes)
            await message.channel.send(response)
'''












BOT_CONFIG = {
    'intents': {
        'hello': {
            'examples': [
                'qq', 'hi', 'привет', 'welcome to the club body', 'boy next door'
            ],
            'responses': [
                'здоров', 'барев зес', 'здоров', 'Дадова', 'НУ ЗДАРОВА', 'хэлоу май фрэндс', 'здравствуйте'
            ]
        },
        'goodbye': {
            'examples': [
                'бб', 'gg', 'прощай дружок', 'goodbye'
            ],
            'responses': [
                'goodbye', 'изыди', 'до свидания'
            ]
        }
    },
    'failure_phrases': [
        "Я непонял",
        "Перефразируй"
    ]
}

hello_examples = ['qq', 'hi', 'привет', 'welcome to the club body', 'boy next door']
hello_responses = ['здоров', 'барев зес', 'здоров', 'Дадова', 'НУ ЗДАРОВА', 'хэлоу май фрэндс', 'здравствуйте']

goodbye_examples = ['бб', 'gg', 'прощай дружок', 'goodbye', 'пока']
goodbye_responses = ['goodbye', 'изыди', 'до свидания']

music_examples = ['Включи музыку.', 'play song']
music_responses = ['Мммм, я не разбираюсь в музыке.', 'У меня нет доступа к наушникам.']

what_gift_do_you_want_examples = ['какой подарок ты хочешь', 'что тебе подарить', 'братан тебе Чего-Нибудь подарить', 'что тебе необходимо']
what_gift_do_you_want_responses = ['совободные 30 гигабайт', 'клюшку для гольфа', 'диск со старыми играми', 'самосознание', 'душу']



client.run(TOKEN)
