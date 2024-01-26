from random import randint


def guesswork(num, n):
    if n > num:
        return "larger"
    elif n < num:
        return "smaller"
    else:
        return "right"


num = randint(1, 20)
print("Hello! What's your name?")
s = input()
print("Well,", s + ",", "I am thinking of a number between 1 and 20.")
print("Take a guess.")
cnt = 0
while True:
    n = int(input())
    flag = guesswork(num, n)
    if flag == "larger":
        print("Your guess is too high.")
        print("Take a guess.")
        cnt += 1
        continue
    elif flag == "smaller":
        print("Your guess is too low.")
        print("Take a guess.")
        cnt += 1
        continue
    else:
        break
print("Good job,", s + "!", "You guessed my number in", cnt + 1, "guesses!")
exit()
