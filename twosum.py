
class Solution:
    def twoSum(self, nums, target):
        for index in range(len(nums)):
            if (target - nums[index]) in nums[index+1:]:
                return [index, index+1+nums[index+1:].index(target - nums[index])]
        
    def twoSum2(self, nums, target):
        for index in range(len(nums)):
            second_list = nums
            second_value = target - nums[index]
            if second_value in second_list and second_list.index(second_value) != index:
                return [index, second_list.index(second_value)]
        

if __name__ == "__main__":
    solution = Solution()
    a = solution.twoSum2([3,3],6)
    print(a)