def find_nine(nums):
    #Remove pass and write your code here
    if 9 in nums:
        index_l=nums.index(9)
        if index_l<4:
            return True
    return False
    

nums=[1,9,4,5,6]
print(find_nine(nums))
