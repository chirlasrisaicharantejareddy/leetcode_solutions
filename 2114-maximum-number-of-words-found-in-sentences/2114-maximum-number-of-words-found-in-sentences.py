class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        MAX=len(sentences[0].split())
        for sentence in sentences:
            print(sentence.split())
            if MAX<len(sentence.split()):
                MAX=len(sentence.split())
        return MAX

        