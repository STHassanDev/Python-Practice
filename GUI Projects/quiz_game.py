def ans(nums,sum):
    for i in range(len(nums)):
        if sum-nums[i] in nums[i+1:]:
            print(f"Pair found: ({nums[i],sum-nums[i]})")
        else:
            print("Pair not Found")

if __name__ == '__main__':
    ans([1,2,3,4],5)
    
