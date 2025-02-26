class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        #check if str1 and str2 are made of the same building block by concatenation them in different orders. 

        if str1 + str2 != str2 + str1:
            return ""

        #find the GCD of the length of both to find the length of the building block.
        max_length = gcd(len(str1), len(str2))

        # return the building block .
        return str1[:max_length]
        