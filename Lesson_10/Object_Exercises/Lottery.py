from random import randint
class Lottery:
    def __init__(self):
        self.high = 45
        self.low= 1
        self.list_of_numbers = self.list_of_numbers()
        self.winner_price = self.winner_price()

    def __str__(self):
        return f"List of numbers {self.list_of_numbers}"

    def list_of_numbers(self):
        numbers = [randint(self.low,self.high) for i in range(6)]
        return numbers

    def winner_price(self):
        num = int(input("Enter the winner price: "))
        return num

    def right_guess(self,guess:int):
        if guess in self.list_of_numbers:
            return True
        else:
            return False

    def winner_amount(self,num_guesses):
        if num_guesses < 2:
            return 0
        if 2<=num_guesses<=5:
            return self.winner_price*self.num_guesses/6
        if num_guesses == 6:
            return self.winner_price


Lot = Lottery()
print(Lot)

count=0
for i in range(6):
    guess = int(input("Guess a number: "))
    if Lot.low<=guess<=Lot.high:
        if Lot.right_guess(guess):
            count+=1
    else:
        print("Invalid guesses")
        print("Your winner price is 0")
        break
else:
    print("You win:",Lot.winner_amount(count))

    def __str__(self):
        return f"{self.list_of_numbers} max win: {self.winner_price}"