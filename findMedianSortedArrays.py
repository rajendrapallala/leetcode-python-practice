from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list3 = nums1 + nums2
        list3.sort()
        index = len(list3) // 2
        if len(list3) % 2 == 0:
            median =  sum(list3[index-1:index+1])/2
        else:
            median = list3[index]
        return median
    def findMedianSortedArrays_binarysort(self, nums1: List[int], nums2: List[int]) -> float:    
        m = len(nums1)
        n = len(nums2)
        minindex = 0
        halflength = (m+n+1)//2
        if m > n:
            listA, listB , maxindex, m, n = nums2, nums1, n, m, n
        else:
            listA, listB , maxindex, m, n = nums1, nums2, m, n, m

        while minindex <= maxindex:
            i = (minindex + maxindex) // 2
            j = halflength - i
            if i > 0 and listA[i-1] > listB[j]:
                maxindex = i - 1
            elif i < n and listB[j-1] > listA[i]:
                minindex = i + 1
            else:
                if i == 0: 
                    maxleft = listB[j-1]
                elif j == 0: 
                    maxleft = listA[i-1]
                else:
                    maxleft = max(listB[j-1],listA[i-1])
                if (m+n)%2 == 1:
                    return maxleft
                if i == n:
                    minright = listB[j]
                elif j == m :
                    minright = listA[i]
                else: 
                    minright = min(listB[j],listA[i])
                return (minright + maxleft)/2.0










if __name__ == "__main__":
    sltn = Solution()
    #print(sltn.findMedianSortedArrays([1,3,5],[2,4]))
    print(sltn.findMedianSortedArrays_binarysort([1,3,5],[2,6,7,9]))
    #print(sltn.findMedianSortedArrays_binarysort([1,3,5],[]))