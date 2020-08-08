class Solution:
    def search(self, nums, target: int) -> bool:
        '''
        [2,2,2,2,2,2,2,5,6,0,0,1,2]
        '''
        if not nums: return False
        left, right = 0, len(nums)-1

        while left<right:
            mid = left + (right - left)//2
            if nums[mid]<nums[right]:
                if nums[mid]<target<=nums[right]:
                    left = mid+1
                elif nums[mid]==target:
                    return True
                else:
                    right = mid-1
            elif nums[mid]>nums[right]:
                if nums[mid]>=target>=nums[left]:
                    right = mid
                else:
                    left = mid+1
            else:
                if target==nums[mid]:
                    return True
                else:
                    right = right - 1

        return True if nums[left]==target else False

if __name__ == '__main__':
    test = Solution()

    data = [2,2,2,2,2,2,2,5,6,0,0,1,2]

    res = test.search(data, 7)

    print(res)




