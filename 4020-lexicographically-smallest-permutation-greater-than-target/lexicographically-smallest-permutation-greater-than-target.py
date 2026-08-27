class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        if len(s) != len(target):
            return ""
        n = len(s)
        freq = [0]*26
        curr = ""

        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        
        for i in range(n-1,-1,-1):
            remain = freq[:]
            greater = True

            for j in range(i):
                x = ord(target[j]) - ord('a')

                if remain[x] == 0:
                    greater = False
                    break
                
                remain[x] -= 1
            if not greater:
                continue

            target_char = ord(target[i]) - ord('a')

            for c in range(target_char + 1, 26):

                if remain[c] == 0:
                    continue

                ans = target[:i]

                ans += chr(ord('a') + c)

                remain[c] -= 1

                for x in range(26):
                    ans += chr(ord('a') + x) * remain[x]

                return ans

        return ""

            


                


        

        