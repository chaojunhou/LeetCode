class Solution:
    def fullJustify(self,words,L):
        i=0
        res=[]
        wordLen=len(words)
        while i<wordLen:
            wordSum=0
            begin=i
            while i<len(words):
                tmp=len(words[i]) if wordSum==0 else wordSum+len(words[i])+1 
                if tmp<=L:
                    wordSum=tmp
                else:
                    break
                i+=1
            spaceCount=L-wordSum
            if i-begin-1>0 and i<len(words):
                everyCount=spaceCount/(i-begin-1)
                spaceCount%=i-begin-1
            else:
                everyCount=0
            j=begin
            s=words[j]
            j+=1
            while j<i:
                s+=' '*(everyCount+1)
                if spaceCount>0 and i<len(words):
                    s+=' '
                    spaceCount-=1
                s+=words[j]
                j+=1
            s+=''*spaceCount
            res.append(s)
        return res
    def fullJustify(self,words,L):
        begin, end = 0, 0   # The index of begin word (inclusive) and end
                            # word (exclusive) in one line
        result =[]
        
        while True:
            wordsLen = 0    # The total length of all words to be used
                            # in this line.  
            # Determine how many following words are used for this line.
            while end < len(words):
                if wordsLen + len(words[end]) + (end - begin) <= L:
                    wordsLen += len(words[end])
                    end += 1
                else:
                    break
            else:
                # This is the last line.
                temp = " ".join(words[begin:end])
                temp += " " * (L - len(temp))
                result.append(temp)
                break
            # Construct the line after text justification.
            temp = ""
            if end == begin + 1:
                # This line only contains one word.
                temp = words[begin] + " " * (L - len(words[begin]))
            else:
                # This line contains multiple words.
                spaceCount = (L - wordsLen) // (end - begin -1)
                oneMoreSpace = (L- wordsLen) % (end- begin - 1)
                
                for index in xrange(begin, end-1):
                    if index - begin < oneMoreSpace:
                        temp += words[index] + " " * (spaceCount + 1)
                    else:
                        temp += words[index] + " " * spaceCount
                temp += words[end-1]
                
            result.append(temp)
            begin = end
        
        return result
            
                    
            
if __name__=='__main__':
    sol=Solution()
    words=["This", "is", "an", "example", "of", "text", "justification."]
    L=16
    from pprint import pprint
    pprint(sol.fullJustify(words,L))
