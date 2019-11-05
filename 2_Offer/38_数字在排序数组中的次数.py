# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 12:02:51 2019

@author: zhe

E-mail: 1194585271@qq.com
"""

#Solution1: O(n) 遍历
class Solution:
    def GetNumberOfK(self, data, k):
        # write code here
        return data.count(k)
    
#Solution2： O(logn) 二分查找找最左边和最右边

class Solution1:
    def GetNumberOfK(self, data, k):
        # write code here
        if not data:
            return 0
        
        firstK = self.GetFirstK(data, k, 0, len(data)-1)
        lastK = self.GetLastK(data, k, 0, len(data)-1)
        
        number = 0
        if firstK > -1 and lastK > -1:
            number =  lastK-firstK+1
            
        return number
    
    def GetFirstK(self, data, k, start, end):
        if start > end:
            return -1
        
        middleIndex = start + (end-start) // 2
        middleData= data[middleIndex]
        
        if middleData < k:
            start = middleIndex + 1
        elif middleData == k :
            if (middleIndex > 0 and data[middleIndex-1] != k) or middleIndex ==0:
                return middleIndex
            else:
                end = middleIndex-1
        else:
            end = middleIndex - 1
            
        return self.GetFirstK(data, k, start, end)

    def GetLastK(self, data, k, start, end):
        if start > end:
            return -1
        
        middleIndex = start + (end-start) // 2
        middleData= data[middleIndex]
        
        if middleData < k:
            start = middleIndex + 1 
        elif middleData == k:
            if (middleIndex < end and data[middleIndex+1] != k) or middleIndex == end:
                return middleIndex
            else:
                start = middleIndex + 1
        else:
            end = middleIndex - 1
            
        return self.GetLastK(data, k, start, end)
    
if __name__ == '__main__':
    test = Solution()
    
    res = test.GetNumberOfK([1,2,3],1)
        
        
     
    