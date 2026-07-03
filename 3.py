class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        hashmap = {}
        for i in range(len(s)):
            if s[i] in hashmap and hashmap[s[i]] >= start:
                start = hashmap[s[i]] + 1
            hashmap[s[i]] = i

            current_window = i - start + 1
            if current_window > longest:
                longest = current_window
        return longest
        
