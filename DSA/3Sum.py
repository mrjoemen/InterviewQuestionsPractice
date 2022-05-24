"""

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

https://leetcode.com/problems/3sum/

"""



class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # need to construct a list of lists that will equate to 0
        # maybe sort the list first, then do a while a loop and under the while loop do the two pointer method
        
        nums.sort()
        answer = []
        
        if len(nums) < 3:
            return answer
        
        for i in range(0, len(nums) - 2):
            anchor = i
            leftPointer = anchor + 1
            rightPointer = len(nums) - 1
            
            while leftPointer < rightPointer:
                currentTriplet = []
                currentSum = nums[anchor] + nums[leftPointer] + nums[rightPointer]
            
                if currentSum < 0:
                    leftPointer += 1
                    
                elif currentSum > 0:
                    rightPointer -= 1
                else:
                    currentTriplet.append(nums[anchor])
                    currentTriplet.append(nums[leftPointer])
                    currentTriplet.append(nums[rightPointer])
                    if currentTriplet not in answer:
                        answer.append(currentTriplet)
                    
                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer + 1]: leftPointer += 1
                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer - 1]: rightPointer -= 1
                    leftPointer += 1
                    rightPointer -= 1
                        
            
        return answer
        