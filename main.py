class Solution:
    def removeElement(nums, val):
        while val in nums:
            nums.remove(val)
        num_elements = len(nums)
        k = f"There are {num_elements} remaining in nums, their values are {nums}"
        print(k)

    removeElement(nums =[0,1,2,2,3,0,4,2], val = 2)
    removeElement(nums = [3,2,2,3], val = 3)