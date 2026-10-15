from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:

    r_counter = Counter(ransomNote)
    m_counter = Counter(magazine)

    print("r_counter: ", r_counter)
    print("m_counter: ", m_counter)

    for char in r_counter:
        if r_counter[char] > m_counter[char]:
            return False
        
        
    
    return True


def canConstructComprehension(ransomNote: str, magazine: str) -> bool:
    m_counter = Counter(magazine)

    return all(m_counter[char] >= count for char, count in Counter(ransomNote).items())


if __name__ == "__main__":
    ransomNote = "a"
    magazine = "b"

    print(canConstruct(ransomNote, magazine))