#!/usr/bin/env python3
'''Task 9's module.
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''' Returns list of tuples.
    '''
    return [(i, len(i)) for i in lst]
