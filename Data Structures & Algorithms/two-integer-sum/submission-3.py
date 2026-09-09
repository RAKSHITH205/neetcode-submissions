class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}

        for i,n in enumerate(nums):
            seen[n]=i

        for i,n in enumerate(nums):
            mid=target-n
            if mid in seen and seen[mid]!=i:
                return[i,seen[mid]]
        return []        


            