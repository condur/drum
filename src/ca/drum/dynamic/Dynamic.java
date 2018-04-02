package ca.drum.dynamic;

import java.util.Arrays;

class Dynamic {

    /**
     * Longest Increasing Sub-sequence - solution for the problem
     */
    static int LongestIncreasingSubsequence(int[] nums) {
        // Initialize the lis array with the len of arr and set all values to 1
        int[] lis = new int[nums.length];
        for (int i = 0; i < lis.length; i++) {
            lis[i] = 1;
        }

        int localMax, maximum = Integer.MIN_VALUE;
        for (int i = 1; i < nums.length; i++) {
            localMax = lis[i];
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    localMax = Math.max(localMax, lis[j] + 1);
                }
            }
            lis[i] = localMax;
            maximum = Math.max(maximum, lis[i]);
        }
        return maximum;
    }

    /**
     * MaxSumIncreasingSubSequence - solution
     */
    static int MaxSumIncreasingSubSequence(int[] nums) {
        // Initialize the msis with a copy of the arr
        int[] msis = Arrays.copyOf(nums, nums.length);

        int localSum, maximum = Integer.MIN_VALUE;
        for (int i = 1; i < nums.length; i++) {
            localSum = msis[i];
            for (int j = 0; j < i; j++) {
                if (nums[j] < nums[i]) {
                    localSum = Math.max(msis[j]+msis[i], msis[i]);
                }
            }
            msis[i] = localSum;
            maximum = Math.max(maximum, msis[i]);
        }
        return maximum;
    }
}
