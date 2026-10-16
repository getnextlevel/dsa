from collections import Counter


def numJewelsInStones(jewels: str, stones: str) -> int:

    if len(jewels) > len(stones) or len(stones) > 50:
        raise ValueError("Length of the arguments violates the contraints")

    counter = Counter(stones)

    return sum([counter[j] for j in jewels])



if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"

    print(numJewelsInStones(jewels, stones))

