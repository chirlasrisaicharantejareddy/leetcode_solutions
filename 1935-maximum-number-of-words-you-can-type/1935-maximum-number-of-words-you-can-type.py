class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words=text.split()
        print(words)
        Total=len(words)
        for word in words:
            for ch in brokenLetters:
                if ch in word:
                    Total=Total-1
                    break
        return Total       