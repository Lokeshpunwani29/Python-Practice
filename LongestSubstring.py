word = "aaaaaaabcda"
start = 0
end = 0
max_len = 0
max_substring = ""
ls = set()

while end < len(word):
    if word[end] not in ls:
        ls.add(word[end])
        # Check if new window is longer
        if end - start + 1 > max_len:
            max_len = end - start + 1
            max_substring = word[start:end+1]  # Store the current max substring
        end += 1
    else:
        ls.discard(word[start])
        start += 1

print("Longest Substring Length:", max_len)
print("Longest Substring:", max_substring)
