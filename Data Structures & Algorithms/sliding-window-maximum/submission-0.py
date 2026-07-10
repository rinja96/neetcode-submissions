'''
Deque approach
==============
- Use deque to store indices of elements in decreasing order in their values.
- Expand window by moving right pointer
    - before inserting the new index, remove indices whose values are smaller than the new value
    - Add new index to the deque
- If left pointer passes the front index, remove it, it's outside window
- Once window reaches a size k, front of the deque represents the maximum -- add to o/p
- Slide the window and repeat 
'''
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        idx = deque()
        left = right = 0

        while right < len(nums):
            while idx and nums[idx[-1]] < nums[right]:
                idx.pop()
            idx.append(right)

            if left > idx[0]:
                idx.popleft()
            
            if (right + 1) >= k:
                output.append(nums[idx[0]])
                left += 1
            right += 1

        return output

