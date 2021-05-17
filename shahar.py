#!/usr/bin/env python3

import numpy as np
import itertools
import random

NUM = 10
SMALL_SET = 10 ** 4

def get_random_permutation(n):
    return np.random.permutation(n)


def check_permutations(perm1, perm2):
    return sum([e1 == e2 for e1, e2 in zip(perm1, perm2)])


def get_random_fit_perm(perm, hits):
    res = []
    while not res:
        res = _get_random_fit_perm(perm, hits)
    return res

def _get_random_fit_perm(perm, hits):
    """
    Bad implementation, if returns empty array should be called again
    """
    n = len(perm)
    assert hits != n-1, f'Thers is no perm that agrees on every index except one.'
    options = set(range(n))
    hits = random.sample(options, hits)
    options = options - set([perm[i] for i in hits])
    res = []
    for i in range(n):
        if i in hits:
            res.append(perm[i])
        else:
            missed_options = tuple(options - set([perm[i]]))
            if len(missed_options) == 0:
                return []
            elem = random.choice(missed_options)
            res.append(elem)
            options -= set([elem])
    return res


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

def generate_all_permutations(n):
    numbers = list(range(n))
    return list(itertools.permutations(numbers))


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
