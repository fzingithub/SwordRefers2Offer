class Solution:
    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        方法一： 三次反转
        [1_最短回文串.py,2,3,4,5,6,7,8,9] k =4
        [4,3,2,1_最短回文串.py,5,6,7,8,9]
        [4,3,2,1_最短回文串.py,9,8,7,6,5]
        [5,6,7,8,9,1_最短回文串.py,2,3,4]
        """
        n=len(nums)
        k=k%n
        def reverse(l,r):
            while(l<r):
                nums[l],nums[r]=nums[r],nums[l]
                l=l+1
                r=r-1
        reverse(0,n-k-1)
        reverse(n-k,n-1)
        reverse(0,n-1)

        def rotate(self, nums, k):
            """
            Do not return anything, modify nums in-place instead.
            方法一： 三次反转
            [1_最短回文串.py,2,3,4,5,6,7,8,9] k =4
            [4,3,2,1_最短回文串.py,5,6,7,8,9]
            [4,3,2,1_最短回文串.py,9,8,7,6,5]
            [5,6,7,8,9,1_最短回文串.py,2,3,4]
            """
            k = k%len(nums)
            nums[:] = nums[-k:] + nums[:-k]


if __name__ == '__main__':
    test = Solution()
    nums = [1,2,3,4,5,6,7]
    test.rotate(nums, 3)
    print(nums)
