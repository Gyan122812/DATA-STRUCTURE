def count_vowel(s, index = 0):
    vowels = "aeiouAEIOU"
    if index == len(s):
        return 0    
    if s[index] in vowels:
        return 1 + count_vowel(s, index + 1)
    else:
        return count_vowel(s, index + 1)
    
s = "Gyanshu Shandilya"
print(count_vowel(s))
