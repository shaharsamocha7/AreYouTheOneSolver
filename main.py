#!/usr/bin/env python3

from constants import NUM, SMALL_SET
from utils import (
    generate_all_permutations, get_random_permutation, get_random_fit_perm, check_permutations,
    get_random_fit_perm)

def smart_guess(options, last_guess, n):
    picked_guess, min_size = [], len(options)
    print (last_guess, len(options))
    for hits in range(n-2):
        guess = get_random_fit_perm(last_guess, hits)
        print(f'guess {guess} for {hits} hits:')
        guess_max_size = 0
        answers = n - 2 if len(options) < SMALL_SET else n // 3
        for answer in range(answers):
            options_teo = len([perm for perm in options if check_permutations(guess, perm) == answer])
            guess_max_size = max(guess_max_size, options_teo)
            print(f'For answer = {answer}, well have {options_teo} options left.')
            if guess_max_size > min_size:
                continue
        if guess_max_size < min_size:
            picked_guess , min_size = guess, guess_max_size
    if len(options) < SMALL_SET:
        for guess in options:
            guess_max_size = 0
        for answer in range(n // 3):
            options_teo = len([perm for perm in options if check_permutations(guess, perm) == answer])
            guess_max_size = max(guess_max_size, options_teo)
            if guess_max_size > min_size:
                continue
            print(f'For answer = {answer}, well have {options_teo} options left.')
        if guess_max_size < min_size:
            picked_guess , min_size = guess, guess_max_size
    print(picked_guess , min_size)
    return picked_guess




def main():
    secret = get_random_permutation(NUM)
    print(f'secret: {secret}')
    permutations = generate_all_permutations(NUM)
    iter = 1
    last_guess = get_random_permutation(NUM)
    while len(permutations) > 1 :
    # for _ in range(10):
        # guess = random.choice(permutations)
        if iter != 1:
            last_guess = smart_guess(permutations, last_guess, NUM)
        hits = check_permutations(secret, last_guess)
        print (f'last_guess: {last_guess}, hits={hits}')
        # print(f'guess={guess}')
        # print(f'hits={hits}')
        if hits == NUM:
            print(f'secret found {last_guess} in {iter} steps.')
        permutations = [
            perm
            for perm in permutations
            if check_permutations(last_guess, perm) == hits]
        iter += 1
        print(len(permutations))
    print(f'guess:  {permutations[0]};\nsecret: {tuple(secret)};\niter={iter}.')


if __name__ == '__main__':
    main()
    # perm = get_random_permutation(NUM)
    # other = get_random_fit_perm(perm, 5)
    # print(f'perm={perm}\n res={other}')
    # print(check_permutations(perm, other))
