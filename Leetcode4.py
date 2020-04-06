class Solution(object):
    def moveZeroes(self, nums):
        new = []
        news = []
        
        for i in range(0,len(nums)):
                    
            if(nums[i] == 0):
                a = nums[i]
                new.append(a)
                             
            if(nums[i] != 0):
                b = nums[i]
                news.append(b)
        
        for j in range(0,len(new)):
            c = new[j]
            news.append(c)
        del nums[:]
        nums.extend(news)
            