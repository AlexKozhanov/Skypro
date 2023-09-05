import random

#объявления переменных
record = 0
list_mix = []
list2 = []
word_j = ""

def mixed_word(word_list):
  """
  Возвращает перемешанное слово в виде списка.
  Параметры: word_list - список
  Возвращает: list_mix - список из перемешанного входной списка
  """
  list_mix.clear()
  for i in range(0, len(word_list)):
      letter = random.choice(word_list) #letter-буква
      word_list.remove(letter)
      list_mix.append(letter)
  return list_mix

def print_statistics(user_name, user_record):
  """
  Записывает результат игрока в файл с конца
  и возвращает максимальный рекорд и кол-во игр
  Параметры: user_name - имя игрока
             user_record - текуший рекорд игрока
  Возвращает: b - список[максимальный рекордб кол-во игр]
  """
  max = 0
  counter = 0
  b = []
  with open('history.txt', 'a', encoding="UTF-8") as file:
      file.write(f"{user_name} {user_record}\n")

  with open('history.txt', 'rt', encoding="UTF-8") as file:
      for line in file:
          counter += 1
          if user_name in line:
              # line = "Игорь 200"
              name = line.split()
              # lst = ['Игорь', '200']
              record = int(name[1])
              if record > max:
                  max = record

  if user_record >= max:
      b.append(user_record)
      b.append(counter)
      return b
  else:
      b.append(max)
      b.append(counter)
      return b

#Основная программа
#Начало
print("Введите ваше имя")
user_input = input()

with open('words.txt', 'rt', encoding="UTF-8") as file:
    for line in file:
        word_list = list(line)
        word_list.pop(-1)
        word_j = "".join(word_list)
        print(f"{word_j} - {word_list}")
        list2 = mixed_word(word_list)

        print('Угадай: ', list2)
        user_print = input()

        if user_print == word_j:
            print("Верно! Вы получаете 10 очков.")
            record += 10
        else:
            print(f"Неверно! Верный ответ – {word_j}.")

a = print_statistics(user_input, record)
print(f"Всего игр сыграно: {a[1]}")
print(f"Максимальный рекорд: {a[0]}")
