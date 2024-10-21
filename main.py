# Guess what the secret word

from random import choice


class SecretWord():
    def __init__(self):
        self.words_to_choose = ['rice', 'corn', 'bean']

    def word_draw(self):
        return choice(self.words_to_choose)

    def word_board(self, word, user_letter, all_letter_typed):
        for letter in word:
            if letter == user_letter or letter in all_letter_typed:
                print(f'{letter}', end="")
            else:
                print("*", end="")

    def play(self):
        attempts = 4
        letter_list = []
        word_drawn = self.word_draw()
        print(f'The word choosed, has {len(word_drawn)} letters')

        while True:
            letter = input("Please, type just one letter:")
            if len(letter) > 1:
                print("You typed more than one letter")
                continue

            if letter not in word_drawn:
                attempts -= 1
            else:
                if letter in letter_list:
                    print("\n Type again, this word exist!!")
                    continue
                letter_list.append(letter)
                self.word_board(word_drawn, letter, letter_list)

            if attempts == 0:
                print("Attempts fineshed!!")
                break

            if all(w in letter_list for w in word_drawn):
                print("\n Congratulation")
                break


if __name__ == '__main__':

    print("======================================================")
    print("=============== Welcome to the game! ==================")
    print("Information:")
    print("You just need to guess the correct word. Good luck")
    print("======================================================")

    sw = SecretWord()
    sw.play()
