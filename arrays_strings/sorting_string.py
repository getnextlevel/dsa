import collections

def sort_string_by_frequency(s):
    counts = collections.Counter(s)

    print("counts: ", counts)

    sorted_counts = counts.most_common()

    print("sorted_counts: ", sorted_counts)

    string_builder = []

    for char, freq in sorted_counts:
        string_builder.append(char * freq)

    print("string_builder :: ", string_builder)

    return "".join(string_builder)



if __name__ == "__main__":
    s = "tree"
    print(sort_string_by_frequency(s))

    s = "cccaaa"
    print(sort_string_by_frequency(s))

    s = "Aabb"
    print(sort_string_by_frequency(s))