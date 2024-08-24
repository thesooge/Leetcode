s = "abciiidef"

k = 3
vowel_count = 0
vowels = ['a','e','i','o','u']
m_vowels = 0
for i in range(k):
    if s[i] in vowels:
        vowel_count+=1
        m_vowels = max(m_vowels,vowel_count)
i=0
for j in range(k,len(s)):
    if s[j] in vowels:
        vowel_count+=1
    if s[i] in vowels and k>1:
        vowel_count-=1
    i+=1
    m_vowels = max(m_vowels,vowel_count)
print(min(m_vowels,k))    