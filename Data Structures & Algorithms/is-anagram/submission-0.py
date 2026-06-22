class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        if sorted_s == sorted_t:
            answer = True
            print("These Strings Match each other !!")
            
        else:
            answer = False
            print("These strings dont match")
        return answer       