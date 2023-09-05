# – это основной файл приложения
from utils import load_random_word
from players import Player

DATA_URL = 'https://api.npoint.io/97b1cf0f7be2004a3a54'

def main():
    print("Введите имя игрока")
    player_name = input()
    player = Player(player_name)

    word = load_random_word(DATA_URL)

    print(f"""Привет, {player_name}!
Составьте {word.count_words()} слов из слова {str.upper(word.get_word())}
Слова должны быть не короче 3 букв"
Чтобы закончить игру, угадайте все слова или напишите 'stop'"
Поехали, ваше первое слово?""")

    while word.count_words() > player.count_words():
        player_word = input()
        if player_word == "стоп" or player_word == "stop":
            print(f"Игра завершена, вы угадали {player.count_words()} слов!")
            print(f"Ваши слова: {', '.join(player.get_word())}")
            break
        elif len(player_word) <= 2:
            print("слишком короткое слово")
        elif word.has_word(player_word) == False:
            print("неверно")
        elif player.has_word(player_word) == False:
            print("уже использовано")
        else:
            print("верно")
            player.add_word(player_word)
            # print(player)
    else:
        print(f"Игра завершена, вы угадали {player.count_words()} слов!")
        print(f"Ваши слова: {', '.join(player.get_word())}")

if __name__ == '__main__':
    main()
