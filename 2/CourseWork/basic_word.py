# - тут класс слова
class BasicWord():
    def __init__(self, word, subword):
        self.word = word            # исходное слово
        self.subword = subword      # набор допустимых слов

    def __repr__(self):
        return f"BasicWord({self.word}, {self.subword})"
        # return f"{self.word}"

    def count_words(self):
        """подсчет количества подслов(вернет int)"""
        subword_numb = len(self.subword)
        return subword_numb

    def has_word(self, player_word):
        """проверку введенного слова в списке допустимых подслов (вернет bool)"""
        if player_word in self.subword:
            return True
        else:
            return False

    def get_word(self):
        """Выводит слово"""
        return self.word
