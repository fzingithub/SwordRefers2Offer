class Solution:
    def search(self, arr, target):
        try:
            return arr.index(target,True)
        except ValueError:
            return -1




    # def search1(self, arr, target):
    #     '''
    #     [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
    #
    #     [16,17,18,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    #
    #     不管反转几下，实际是只反转了一下
    #
    #     假设数组元素原先是按升序排列的。若有多个相同元素，返回索引值最小的一个。
    #
    #     [2,2,2,2,2,2,2,5,6,0,0,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
    #     '''
    #     if not arr: return -1
    #     left, right = 0, len(arr) - 1
    #     flag = 0
    #     while left < right:
    #         mid = left + (right - left) // 2
    #         if arr[mid] < arr[right]: #右边有序
    #             if arr[mid] < target < arr[right]:
    #                 left = mid + 1
    #             elif arr[mid] == target: # mid是，左边有可能还有target
    #                 right = mid
    #             elif arr[right] == target:
    #                 flag = 1
    #                 resStorage = right  # 存起来
    #                 right = right - 1  # 右边界边界移进一步
    #             else:
    #                 right = mid - 1 # target 在左边
    #         elif arr[mid] > arr[right]: # 左边有序
    #             if arr[mid] >= target >= arr[left]:
    #                 right = mid   # target 在左边]
    #             else:
    #                 left = mid + 1 # target (在右边
    #         else:
    #             if target == arr[mid]:
    #                 right = mid    # target 在左边]
    #             else:
    #                 right = right - 1  # # 右边界边界移进一步
    #
    #     resStorage = resStorage if flag else -1 # 看有没有存下临时答案
    #     return left if arr[left] == target else resStorage








if __name__ == '__main__':
    test = Solution()
    arr = [4,5,5,5,1,2,3,4]
    target = 5
    res = test.search(arr, target)

    print(res)

