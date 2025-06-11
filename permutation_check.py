def check_freq(freq, win_freq):
    for i in range(26):
        if freq[i] != win_freq[i]: return False
    
    return True

def check_inclusion(s1, s2):
    freq = [0] * 26 # Creates a list of 26 Element
    for i in range(len(s1)):
        freq[int(ord(s1[i])) - ord('a')]+=1 # ord return ASCII value while our int() constructs int value
    
    win_size = len(s1)
    
    for i in range(len(s2)):
        win_time = 0
        win_idx = i
        win_freq = [0] * 26
        while(win_time < win_size and win_idx < len(s2) ):
            win_freq[int(ord(s2[win_idx])) - ord('a')]+=1
            win_time+=1
            win_idx+=1
            
        if check_freq(freq , win_freq): return True
    
    return False

def main():
    str1 = str(input("Enter the String to be checked:"))
    str2 = str(input("Enter the String in which checked:"))
    res = check_inclusion(str1, str2)
        
    if res : print("Permutation is found :)")
    else : print("Not Found :(")

main()

"""
def check_inclusion(s1, s2):
    from collections import Counter

    len1, len2 = len(s1), len(s2)
    if len1 > len2:
        return False

    # Frequency of characters in s1
    freq_s1 = Counter(s1)

    # First window frequency
    window = Counter(s2[:len1])

    if window == freq_s1:
        return True

    # Slide the window
    for i in range(len1, len2):
        start_char = s2[i - len1]
        new_char = s2[i]

        window[new_char] += 1
        window[start_char] -= 1

        if window[start_char] == 0:
            del window[start_char]

        if window == freq_s1:
            return True

    return False


def main():
    str1 = input("Enter the String to be checked: ")
    str2 = input("Enter the String in which checked: ")
    res = check_inclusion(str1, str2)

    if res:
        print("Permutation is found :)")
    else:
        print("Not Found :(")

main()
"""
