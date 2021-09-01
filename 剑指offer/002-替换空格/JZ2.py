class Solution:
    def replaceSpace(self , s ):
        # create a new empty str, loop the input string
        # if blank -> new string add "%20"
        # if not black -> keep the str
        gen = str()
        for i in s:
            if i == " ":
                gen += "%20"
            else:
                gen += i
        return gen