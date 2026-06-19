class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """


        ptrA = m-1 ## nums1
        ptrB = m+n-1 ## nums1
        ptrC = n-1 

        while ptrA >= 0 and ptrC >= 0:
            if nums1[ptrA] > nums2[ptrC]:
                nums1[ptrB] = nums1[ptrA]  ## overwrite it 
                ptrA -= 1
            else:
                nums1[ptrB] = nums2[ptrC]
                ptrC -= 1
            ptrB -= 1
        
        while ptrC >= 0:
            nums1[ptrB] = nums2[ptrC]
            ptrC -= 1
            ptrB -= 1
        print(nums1)
        