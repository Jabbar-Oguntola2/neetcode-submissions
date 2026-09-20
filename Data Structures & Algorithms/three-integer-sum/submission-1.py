class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Sort the list 
        # make two nested loops
        # i with inital value
        # j checking next two
        # if i + j + (j + 1) = 0 add the tuple to output array
        # not adjust j until j reaches end of list
        # then repeat with new i

        output = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threesum = num + nums[l] + nums[r]
                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    output.append([num, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1

        return output

            

        
           

            