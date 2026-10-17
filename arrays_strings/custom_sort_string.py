def customSortString(order: str, s: str) -> str:
    order_idx = {}
    s_chars = list(s)

    print("s_chars before: ", s_chars)
    count = 0
    
    for char in s:
        # print("idx, char: ", idx, char)
        # s_idx[char] = idx

        if char in order:
            s_chars.remove(char)
            count += 1

    print("count : ", count)
    

    print("s_chars after: ", s_chars)
    print("order[:count + 1]: ", order[:count + 1])
    return order[:count] + "".join(s_chars)
    


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