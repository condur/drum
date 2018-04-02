package ca.drum.dynamic;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class DynamicTest {

    @Test
    void LISTest() {
        int[] nums = new int[]{10, 22, 9, 33, 21, 50, 41, 60, 80};
        int want = 6;
        int got = Dynamic.LongestIncreasingSubsequence(nums);
        assertEquals(want, got);
    }

    @Test
    void MSISTest() {
        int[] nums = new int[]{1, 101, 2, 3, 100, 4, 5};
        int want = 106;
        int got = Dynamic.MaxSumIncreasingSubSequence(nums);
        assertEquals(want, got);
    }
}
