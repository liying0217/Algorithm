class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return False
        dict={}
        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]],i]
            else:
                dict[target-nums[i]]=i


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution().twoSum(nums, target)
    print(s)