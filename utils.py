import itertools
import numpy as np
import random

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
    Bad implementation, if returns empty array should be called via _get_random_fit_perm().
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


def generate_all_permutations(n):
    numbers = list(range(n))
    return list(itertools.permutations(numbers))
