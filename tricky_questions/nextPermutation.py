def nextNumber(nums):
        idx = -1
        for i in range(len(nums)-1, 0,-1):
            if nums[i] > nums[i-1]:
                idx = i - 1
                break
        if idx == -1:
            nums.sort()
            return
        idx2 = idx+1
        for i in range(idx +1, len(nums)):
            if nums[i] > nums[idx]:
                idx2 = i
        
        nums[idx], nums[idx2] = nums[idx2], nums[idx]
        nums[idx+1:len(nums)] = sorted(nums[idx+1:len(nums)])
        return
x = "5730126984"
nums = [int(i) for i in x]
print(nums)
nextNumber(nums)
print(nums)
