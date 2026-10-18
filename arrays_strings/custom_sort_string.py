def customSortString(order: str, s: str) -> str:
    result = list(s)

        # Sort using the index in order as the key
    result.sort(key=lambda c: order.index(c) if c in order else len(order))
    return ''.join(result)


# Simplified version (same idea, no lambda, no repeated order.index scans):
#
# def customSortString(order: str, s: str) -> str:
#     # rank of each char = its position in order, e.g. "cba" -> {c: 0, b: 1, a: 2}
#     rank = {char: i for i, char in enumerate(order)}
#
#     # chars not in order go last, so give them a rank past the end
#     missing = len(order)
#
#     # sort s by rank, then join the sorted chars back into a string
#     return ''.join(sorted(s, key=lambda c: rank.get(c, missing)))
#
# Even simpler, with no lambda at all (count each char, emit in order):
#
# from collections import Counter
#
# def customSortString(order: str, s: str) -> str:
#     counts = Counter(s)
#     result = ''
#
#     for char in order:                  # chars in the custom order first
#         result += char * counts.pop(char, 0)
#
#     for char, count in counts.items():  # whatever is left, in any order
#         result += char * count
#
#     return result


if __name__ == "__main__":
    order = "cba"
    s = "abcd"

    print(customSortString(order, s))

    order = "bcafg"
    s = "abcd"

    print(customSortString(order, s))


    order = "kqep"
    s = "pekeq"

    print(customSortString(order, s))