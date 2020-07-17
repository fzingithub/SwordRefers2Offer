# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 14:03:49 2019

@author: zhe

E-mail: 1194585271@qq.com
"""
#solution 1：nlogn 排序 记录
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0 or numbers == None:
            return 0
        elif len(numbers) == 1:
            return numbers[0]
        numbers.sort()     #python  内置的排序方法为 Timsort 时间：O(n) O(nlogn) O(nlogn) 空间：O(n)   
        
        oldNum = numbers[0]
        counter = 1
        for i in range(1,len(numbers)):
            if numbers[i]==oldNum:
                counter = counter + 1
                if counter>len(numbers)/2:
                    return numbers[i]
            else:
                oldNum = numbers[i]
                counter = 1
        return 0

#solution 2； 基于partition函数的O(n)算法
class Solution1:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0 or numbers == None:
            return 0
        elif len(numbers) == 1:
            return numbers[0]
        
        middle = len(numbers)//2
        start = 0
        end = len(numbers)-1
        
        index = self.Partition(numbers,start,end)
        while index != middle:
            if index > middle:
                end = index - 1
                index = self.Partition(numbers,start,end)
            else:
                start = index + 1
                index = self.Partition(numbers,start,end)
                
        result = numbers[middle]
        if not self.checkKMoreThanHalf(numbers,result):
            result = 0
            
        return result
    
    def Partition(self,numbers,start,end):
        left = start
        right = end
        #最左侧为参考值
        k = numbers[left]
        #当left下标，小于right下标的情况下，此时判断二者移动是否相交，若未相交，则一直循环
        while left < right:
            #当left对应的值小于k参考值，就一直向右移动
            while left <= end and numbers[left] <= k:
                left = left + 1
            #当right对应的值大于k参考值，就一直向左移动
            while right >= start and numbers[right] > k:
                right = right -1
            #若移动完，二者仍未相遇则交换下标对应的值
            if left < right:
                numbers[left],numbers[right] = numbers[right],numbers[left]
                
            #若移动完，已经相遇，则交换right对应的值(k的最终位置) 和参考值
        numbers[right],numbers[start] = numbers[start],numbers[right]
            
        return right #返回具体位置索引
        
    def checkKMoreThanHalf(self,numbers,result):
        counter = 0
        for i in range(len(numbers)):
            if numbers[i] == result:
                counter = counter + 1
                if counter > len(numbers)/2:
                    return True
        return False
        
        
            
#solution 3； 根据数组的特点找出O(n)的算法
class Solution2:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if len(numbers) == 0 or numbers == None:
            return 0
        elif len(numbers) == 1:
            return numbers[0]
        
        result = numbers[0]
        times = 1 
        
        for i in range(1,len(numbers)):
            if times == 0:
                result = numbers[i]
                times = 1
            elif numbers[i] == result:
                times = times + 1
            else:
                times = times - 1
        
        if not self.checkKMoreThanHalf(numbers,result):
            return 0
        
        return result
        
                
    def checkKMoreThanHalf(self,numbers,result):
        counter = 0
        for i in range(len(numbers)):
            if numbers[i] == result:
                counter = counter + 1
                if counter > len(numbers)/2:
                    return True
        return False            

if __name__ == '__main__':
    test = Solution2()
    
    a = test.MoreThanHalfNum_Solution([4,2,1,4,4,4])
    
            
            
        
        