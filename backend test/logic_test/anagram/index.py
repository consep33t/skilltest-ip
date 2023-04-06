def is_anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    if len(str1) != len(str2):
        return "not an anagram"
    
    char_freq = {}
    
    for char in str1:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
    
    for char in str2:
        if char in char_freq:
            char_freq[char] -= 1
        else:
            return "not an anagram"
    
    for value in char_freq.values():
        if value != 0:
            return "not an anagram"
    
    return "is anagram"


str1 = input("Masukkan kata pertama: ")
str2 = input("Masukkan kata kedua: ")

print(str1, "dan", str2, "=>", is_anagram(str1, str2))
