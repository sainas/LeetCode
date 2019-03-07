class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        if len(A) == 1:
            return [letter for letter in A[0]]
        dict1={}
        for letter in A[0]:
            dict1[letter]=dict1.get(letter,0)+1
        dict2 = dict1.copy()
        for str1 in A[1:]:
            for letter in str1:
                dict2[letter]=dict2.get(letter,-105)-1
            for k in [*dict2]:
                if dict2[k]==dict1.get(k,'None'):
                    dict1.pop(k, None)
                elif dict2[k]>0:
                    dict1[k]=dict1[k]-dict2[k]
            dict2=dict1.copy()
        result=[]
        for k in [*dict1]:
            for i in range(dict1[k]):
                result.append(k)
        return result