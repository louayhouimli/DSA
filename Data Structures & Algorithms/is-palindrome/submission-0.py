class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        i = 0
        j = len(alpha) -1
        while i<j:
            if alpha[i] != alpha[j]:
                return False
            i+=1
            j-=1
        return True