from typing import List


def build_np_such_as_np_patterns(n=5) -> List[List[object]]:
    """Builds a list of n such as patterns.
    NP0 such as {NP1, NP2,..., (and | or )} NPn

    Args:
        n (int): Number of NP patterns to include in the such as pattern.

    Returns:
        list: List of such as patterns.
    """
    patterns = []
    for i in range(n):
        pattern = [
            {"POS": {"IN": ["NOUN", "PROPN"]}},
            {"ORTH": ",", "OP": "?"},
            {"LOWER": "such"},
            {"LOWER": "as"},
        ]
        pattern += [
            {"POS": {"IN": ["NOUN", "PROPN"]}},
            {"ORTH": ","},
        ] * i
        pattern += [] if i == 0 else [{"LOWER": {"IN": ["and", "or"]}}]
        pattern += [{"POS": {"IN": ["NOUN", "PROPN"]}}]
        patterns.append(pattern)
    return patterns


def build_such_np_as_np_patterns(n=5) -> List[List[object]]:
    """Builds a list of n such as patterns.
    Such NP as {NP,}* {( and | or )} NP

    Args:
        n (int): Number of NP patterns to include in the such as pattern.

    Returns:
        list: List of such as patterns.
    """
    patterns = []
    for i in range(n):
        pattern = [
            {"LOWER": "such"},
            {"POS": {"IN": ["NOUN", "PROPN"]}},
            {"LOWER": "as"},
        ]
        pattern += [
            {"POS": {"IN": ["NOUN", "PROPN"]}},
            {"ORTH": ","},
        ] * i
        pattern += [] if i == 0 else [{"LOWER": {"IN": ["and", "or"]}}]
        pattern += [
            {"POS": {"IN": ["NOUN", "PROPN"]}},
        ]
        patterns.append(pattern)
    return patterns
