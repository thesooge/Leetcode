def lengthOfLongestSubstring(s):
    li_hash = {}

    i = 0
    j = 0
    max_length = 0

    while j<len(s):
        if s[j] not in li_hash:
            li_hash[s[j]] = 1
            j += 1
            max_length = max(max_length, j - i)
        else:
            del li_hash[s[i]]
            i += 1

    return max_length        


s = "abcabcbb"

print(lengthOfLongestSubstring(s)) 