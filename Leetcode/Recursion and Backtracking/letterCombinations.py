class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        mapp = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        def helper(i, subset):
            if len(subset) == len(digits):
                if subset:
                    ans.append("".join(subset[:]))
                return

            
            for c in mapp[digits[i]]:
                subset.append(c)
                helper(i + 1, subset)
                subset.pop()


        ans = []
        helper(0, [])
        return ans