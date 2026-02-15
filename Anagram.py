# Status -> Done

def isAnagram(str1, str2):
    string1 = str1.replace(" ","").lower()
    string2 = str2.replace(" ","").lower()

    return sorted(string1)==sorted(string2)

s1 = input("Enter First String: ")
s2 = input("Enter Second String: ")

result = isAnagram(s1, s2) if "Anagram" else "Not Anagram"
print(result)