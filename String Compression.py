chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]


class Solution:
    def compress(self, chars: List[str]) -> int:
        write_index = 0
        i = 0

        while i < len(chars):
            char = chars[i]
            count = 1

            while i + 1 < len(chars) and chars[i+1] == char:
                count += 1
                i += 1

            chars[write_index] = char
            write_index += 1

            if count > 1:
                for c in str(count):
                    chars[write_index] = c
                    write_index += 1
            i += 1
        
        return write_index



# chars_count = {}
# s = ""
# for i in range(len(chars)):
#     if chars[i] in chars_count:
#         chars_count[chars[i]] += 1
#     else:    
#         chars_count[chars[i]] = 1


# for i in range(len(chars)):
#     if chars_count[chars[i]] == 1:
#         s += chars[i]
#     else:
#         if chars[i] not in s:
#             s += chars[i]
#             for j in str(chars_count[chars[i]]):
#                 s += j

# print(len(s))

