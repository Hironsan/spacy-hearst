from typing import Any, List


def build_np_such_as_np_patterns(n=5) -> List[Any]:
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


def build_such_np_as_np_patterns(n=5) -> List[Any]:
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


def build_np_or_and_other_np_patterns(n=5) -> List[Any]:
    """Builds a list of np or/and other patterns.
    NP {, NP}* {,} or other NP

    Args:
        n (int): Number of NP patterns to include in the pattern.

    Returns:
        list: List of patterns.
    """
    patterns = []
    for i in range(n):
        pattern = [
            {"POS": {"IN": ["NOUN", "PROPN"]}},
        ]
        pattern += [
            {"ORTH": ","},  # type: ignore
            {"POS": {"IN": ["NOUN", "PROPN"]}},
        ] * i
        pattern += [
            {"ORTH": ",", "OP": "?"},  # type: ignore
            {"LOWER": {"IN": ["or", "and"]}},
            {"LOWER": "other"},  # type: ignore
            {"POS": {"IN": ["NOUN", "PROPN"]}},
        ]
        patterns.append(pattern)
    return patterns
