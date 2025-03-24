def count_vowel(s, index = 0):
    vowelS = "aeiouAEIOU"
    if index == len(s):
        return 0    
    if s[index] in vowelS:
        return 1 + count_vowel(s, index + 1)
    else:
        return count_vowel(s, index + 1)
    
s = "Hello, World!"
print(count_vowel(s))
