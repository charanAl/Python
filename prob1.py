class Solution:
    def twoSum(self, num:list(int), target:int)-> list[int]:
        num_dict = {}

        for i, num in enumerate(num):
            complement = target -num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
        return[]