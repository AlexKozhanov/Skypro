# - тут лежат функции
import random
import requests
from basic_word import BasicWord

def load_random_word(path):
    """ - получит список слов с внешнего ресурса,
        - выберет случайное слово,
        - создаст экземпляр класса `BasicWord`,
        - вернет этот экземпляр."""
    data = requests.get(path)

    all_words = data.json()
    random_word = random.choice(all_words)

    basic_word = BasicWord(random_word['word'], random_word['subwords'])

    return basic_word
