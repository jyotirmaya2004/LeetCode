class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        
        if(len(bits) == 1):
            return True
        
        i = 0
        while(True):

            if(bits[i] == 0):
                i += 1
            else:
                i += 2
            
            if(i == len(bits) - 1):
                return True
            elif(i == len(bits)):
                return False