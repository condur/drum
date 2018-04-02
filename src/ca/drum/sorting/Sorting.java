package ca.drum.sorting;

class Sorting {

    /**
     * Find the index of the min item in the array
     */
    static int MinIndex(int[] nums, int startIndex) {
        int minIndex = startIndex, min = nums[startIndex];
        for (; startIndex < nums.length; startIndex++) {
            if (min > nums[startIndex]) {
                minIndex = startIndex;
                min = nums[startIndex];
            }
        }
        return minIndex;
    }

    /**
     * Swaps two elements of an array.
     */
    private static void Swap(int[] arr, int i, int j) {
        int t = arr[i];
        arr[i] = arr[j];
        arr[j] = t;
    }

    /**
     * Selection - the algorithm sorts an array by repeatedly finding the minimum element
     * (considering ascending order) from unsorted part and putting it at the beginning.
     */
    static int[] Selection(int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            int minIndex = MinIndex(nums, i);
            Swap(nums, minIndex, i);
        }
        return nums;
    }

    /**
     * Bubble -  is the simplest sorting algorithm that works by repeatedly swapping
     * the adjacent elements if they are in wrong order.
     */
    static int[] Bubble(int[] nums) {
        for (int i = 0; i < nums.length - 1; i++) {
            boolean swapped = false;
            for (int j = 0; j < nums.length - i - 1; j++) {
                if (nums[j] > nums[j + 1]) {
                    Swap(nums, j, j + 1);
                    swapped = true;
                }
            }
            if (!swapped) break;
        }
        return nums;
    }

    /**
     * Insertion - is a simple sorting algorithm that builds the final sorted array one item at a time.
     */
    static int[] Insertion(int[] nums) {
        int key;
        for (int i = 1; i < nums.length; i++) {
            key = nums[i];
            int j = i - 1;
            while (j >= 0 && nums[j] > key) {
                nums[j + 1] = nums[j];
                j--;
            }
            nums[j + 1] = key;
        }
        return nums;
    }
}
