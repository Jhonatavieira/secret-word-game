# Guess what the secret workd

# from random import choices


class SecretWord():
    def __init__(self):
        pass
        ...  # self.words_to_choose = ['Banana', 'uva']

    def word_draw(self):
        print('teste')
        ...  # return choices(self.words_to_choose)

    def word_board(self):
        ...

    def play(self):
        w = SecretWord.word_draw()
        print(w)


if __name__ == '_main_':
    sw = SecretWord
    sw.play()
