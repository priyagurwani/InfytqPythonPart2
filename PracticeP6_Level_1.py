def list123(nums):
    #start writing your code here
    string=''
    for i in nums:
        string=string+str(i)
        if "123" in string:
            return True
    return False

    

nums=[1,2,3,4,5]
print(list123(nums))
