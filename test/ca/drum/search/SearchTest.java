package ca.drum.search;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.assertEquals;

class SearchTest {

    @Test
    void LinearTest() {
        int[] nums = new int[]{1, 101, 2, 3, 100, 4, 5};

        int want = 2;
        int got = Search.Linear(2, nums);
        assertEquals(want, got);

        want = -1;
        got = Search.Linear(10000, nums);
        assertEquals(want, got);
    }

    @Test
    void BinaryV1Test() {
        int[] nums = new int[]{1, 2, 3, 4, 5, 6};

        int want = 1;
        int got = Search.BinaryV1(2, nums);
        assertEquals(want, got);

        want = -1;
        got = Search.BinaryV1(10000, nums);
        assertEquals(want, got);
    }

    @Test
    void BinaryV2Test() {
        int[] nums = new int[]{1, 2, 3, 4, 5, 6};

        int want = 1;
        int got = Search.BinaryV2(2, nums);
        assertEquals(want, got);

        want = -1;
        got = Search.BinaryV2(10000, nums);
        assertEquals(want, got);
    }

    @Test
    void SqrtTest() {
        int want = 2;
        int got = Search.Sqrt(4);
        assertEquals(want, got);

        want = 3;
        got = Search.Sqrt(9);
        assertEquals(want, got);

        want = 46340;
        got = Search.Sqrt(2147483647);
        assertEquals(want, got);
    }
}
