class Solution:
    def isPalindrome(self, x: int) -> bool:
        self.new_num = x
        self.remainer = 0
        if x < 0 :
            return False
        while x != 0:
            self.remainer += x % 10
            self.remainer *= 10 
            x = x // 10 
    
        if self.remainer/10 ==  self.new_num: 
            return True
        return False





obj1 = Solution()
print(obj1.isPalindrome(121))