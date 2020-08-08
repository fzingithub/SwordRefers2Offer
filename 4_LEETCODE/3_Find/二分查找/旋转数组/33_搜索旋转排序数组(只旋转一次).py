class Solution:
    def search(self, nums, target):
        '''
        [0,1,2,3,4,5,6,7]
        [6,7,0,1,2,3,4,5]
        '''
        if not nums: return -1
        left, right = 0, len(nums)-1

        while left<right:
            mid = left + (right-left)//2

            if nums[mid]>nums[right]:
                if nums[mid]>=target>=nums[left]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid + 1
                elif nums[mid]==target:
                    return mid
                else:
                    right = mid - 1

        return left if nums[left]==target else -1

if __name__ == '__main__':
    test = Solution()
    data = [6,7,0,1,2,3,4,5]
    res = test.search(data, 5)

    print(res)




