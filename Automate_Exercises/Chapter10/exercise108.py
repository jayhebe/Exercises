import random, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
# logging.disable(logging.CRITICAL)

guess = ""
while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
    
toss = random.randint(0, 1)

if toss == 0:
    toss = "heads"
elif toss == 1:
    toss = "tails"

if toss == guess:
    logging.debug("toss is " + toss + ", guess is " + guess)
    print("You got it!")
else:
    logging.debug("toss is " + toss + ", guess is " + guess)
    print("Nope! Guess again!")
    guess = input()
    
    if toss == guess:
        logging.debug("toss is " + toss + ", guess is " + guess)
        print("You got it!")
    else:
        logging.debug("toss is " + toss + ", guess is " + guess)
        print("Nope. You are really bad at this game.")