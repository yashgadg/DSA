

def naive_string_match(text, pattern):
    n = len(text)
    m = len(pattern)
    occurrences = []

   
    for i in range(n - m + 1):
        match = True
        for j in range(m):
            if text[i + j] != pattern[j]:
                match = False
                break
        if match:
            occurrences.append(i)

    return occurrences


if __name__ == "__main__":
    text = input("Enter the text string: ")
    pattern = input("Enter the pattern string: ")

    indices = naive_string_match(text, pattern)

    if indices:
        print("Pattern found at indices:", indices)
    else:
        print("Pattern not found in the text.")

