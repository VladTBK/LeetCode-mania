class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x_list = [i for i in str(x)]
        n = round(len(x_list)/2)

        for i in range(n):
            if(x_list[i] != x_list[-i-1]):
                return False
        return True
            
        
