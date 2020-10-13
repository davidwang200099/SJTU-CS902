"""Simulating the dice game Craps."""
import random

maxtimes=500
money=10000
moneypertime=100

win=(7, 11)
lose=(2, 3, 12)

def roll_dice():
    """Roll two dice and return their face values as a tuple."""
    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    return (die1, die2)  # pack die face values into a tuple

def display_dice(dice):
    """Display one roll of the two dice."""
    die1, die2 = dice  # unpack the tuple into variables die1 and die2
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')

# continue rolling until player wins or loses
#while money>0 and times<maxtimes:
for i in range(maxtimes):
    if money<0:
        print("Player plays for %d times"%i)
        exit(0)
    die_values = roll_dice()

    sum_of_dice = sum(die_values)
    if sum_of_dice in win:  # win
        money+=moneypertime
    elif sum_of_dice in lose:  # lose
        money-=moneypertime
    else:  
        pass

print("Player has %d dollars at last"%money)


