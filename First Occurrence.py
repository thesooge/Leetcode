haystack = "wasabutsad"

needle = "sad"

new_str = ""


for i in range(len(haystack)):
    if needle[0] == haystack[i]:
        if needle == haystack[i:len(needle)+i]:
            print(haystack.index(needle))



