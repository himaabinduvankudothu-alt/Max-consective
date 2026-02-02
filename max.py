
def longestOnes(nums, k):
        l=0
        ml=0
        z=0
        for r in range(len(nums)):
            if nums[r]==0:
                z+=1
            while z>k:
                if nums[l]==0:
                    z-=1
                l+=1
            ml=max(ml,r-l+1)
        return ml
