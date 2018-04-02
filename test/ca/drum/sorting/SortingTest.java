package ca.drum.sorting;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

class SortingTest {

    @Test
    void MinIndexTest() {
        int[] nums = new int[]{2, 4, 3, 6, 5};
        int minIndex = Sorting.MinIndex(nums, 0);
        assertEquals(0, minIndex);

        minIndex = Sorting.MinIndex(nums, 2);
        assertEquals(2, minIndex);

        minIndex = Sorting.MinIndex(nums, 3);
        assertEquals(4, minIndex);
    }

    @Test
    void SelectionTest(){
        int[] nums = new int[]{2, 4, 3, 6, 5};
        int[] numsSorted = new int[]{2, 3, 4, 5, 6};
        var result = Sorting.Selection(nums);
        assertArrayEquals(numsSorted, result);
    }

    @Test
    void BubbleTest(){
        int[] nums = new int[]{2, 4, 3, 6, 5};
        int[] numsSorted = new int[]{2, 3, 4, 5, 6};
        var result = Sorting.Bubble(nums);
        assertArrayEquals(numsSorted, result);
    }

    @Test
    void InsertionTest(){
        int[] nums = new int[]{2, 4, 3, 6, 5};
        int[] numsSorted = new int[]{2, 3, 4, 5, 6};
        var result = Sorting.Insertion(nums);
        assertArrayEquals(numsSorted, result);
    }
}

