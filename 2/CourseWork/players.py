# - тут класс игрока
class Player():
    def __init__(self, name):
        self.name = name                    # имя пользователя
        self.subword = []                   # использованные слова пользователя
        # self.player_word = player_word      # слово вводимое пользователем

    def __repr__(self):
        return f"Player({self.name}, {self.subword})"

    def count_words(self):
        """получение количества использованных слов (возвращает int)"""
        subword_numb = len(self.subword)
        return subword_numb

    def add_word(self, player_word):
        """добавление слова в использованные слова (ничего не возвращает)"""
        self.subword.append(player_word)
        return

    def has_word(self, player_word):
        """проверка использования данного слова до этого (возвращает bool)"""
        if player_word in self.subword:
            return False
        else:
            return True

    def get_name(self):
        """Выводит имя игрока"""
        return self.name

    def get_word(self):
        """Выводит слова игрока"""
        return self.subword