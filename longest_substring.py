class Solution:
    def lengthOfLongestSubstring_little_slower(self, s: str) -> int:
        len1 = 0
        len2 = 0
        sub_string = []
        for char in s:
            if char in sub_string:
                len2 = len1 if len1 > len2 else len2
                start_index = sub_string.index(char)
                sub_string = sub_string[start_index+1:]
                sub_string.append(char)
                len1 = len(sub_string)
            else:
                sub_string.append(char)
                len1 = len(sub_string)
        return len1 if len1 > len2 else len2       
    def lengthOfLongestSubstring_little_slower_simplified(self, s: str) -> int:
        str_list = []
        max_length = 0
    
        for x in s:
            if x in str_list:
                start = str_list.index(x)+1
                str_list = str_list[start:]
            
            str_list.append(x)    
            max_length = max(max_length, len(str_list))        
    def lengthOfLongestSubstring(self, s: str) -> int:        
        dct = {}
        max_so_far = curr_max = start = 0
        for index, i in enumerate(s):
            if i in dct and dct[i] >= start:
                max_so_far = max(max_so_far, curr_max)
                curr_max = index - dct[i]
                start = dct[i] + 1
            else:
                curr_max += 1
            dct[i] = index
        return max(max_so_far, curr_max)        

if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring('dvdf'))   #3
    print(solution.lengthOfLongestSubstring('abcabcbb'))   #3 
    print(solution.lengthOfLongestSubstring('pwwcvw'))   #3     