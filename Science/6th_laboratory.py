###
Вариант: 10
Текст задачи: Дана строка-предложение на английском языке. Преобразовать 
строку так, чтобы каждое слово начиналось с заглавной буквы
###
N = 'O sweetest Jesus, save us. Sweetest Jesus Christ, Jesus, open to me the door of repentance, O Jesus.'
words = N.split()
capitalized_words = [word.capitalize() for word in words]
capitalized_sentence = " ".join(capitalized_words)
print(capitalized_sentence)
