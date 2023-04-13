import os
import random
from constants import BASE_DIR


def generate_random_voice(directory_name):
    count = len(
        [entry for entry in os.listdir(BASE_DIR + f"\{directory_name}") if
         os.path.isfile(os.path.join(BASE_DIR + f"\{directory_name}", entry))])
    random_voice = random.randint(1, count)
    return random_voice
