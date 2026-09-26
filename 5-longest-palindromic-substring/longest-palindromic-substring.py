class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        if not s: return ""

        def expandAroundCenter(left: int, right: int) -> str:
            # Expand while in bounds and characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindromic substring
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Check odd length palindromes (single char center)
            odd_pal = expandAroundCenter(i, i)
            # Check even length palindromes (center between two chars)
            even_pal = expandAroundCenter(i, i + 1)

            # Update longest found so far
            if len(odd_pal) > len(longest):
                longest = odd_pal
            if len(even_pal) > len(longest):
                longest = even_pal

        return longest