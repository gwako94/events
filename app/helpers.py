import random
import string

def generate_id():
    letters = list(string.ascii_letters)
    numbers = list(string.digits)

    random_id = random.sample(numbers, 4) + random.sample(letters, 2)
    random.shuffle(random_id)
    generated_id = "".join(random_id)
    return generated_id
