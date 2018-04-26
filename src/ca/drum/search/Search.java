package ca.drum.search;

class Search {

    /**
     * Linear - find if item x exists is the array, return the index of the item or -1
     */
    static int Linear(int target, int[] nums) {
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == target) {
                return i;
            }
        }
        return -1;
    }

    /**
     * Binary - find if an item exists is the array, return the index of the item or -1
     */
    static int BinaryV1(int target, int[] nums) {
        int lo = 0, hi = nums.length - 1;
        while (lo <= hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }
        }
        return -1;
    }

    /**
     * Binary - find if an item exists is the array, return the index of the item or -1
     */
    static int BinaryV2(int target, int[] nums) {
        int lo = 0, hi = nums.length;
        while (lo < hi) {
            int mid = lo + (hi - lo) / 2;
            if (nums[mid] == target) {
                return mid;
            } else if (nums[mid] < target) {
                lo = mid + 1;
            } else {
                hi = mid;
            }
        }

        // Post-processing:
        // End Condition: left == right
        if (lo != nums.length && nums[lo] == target) {
            return lo;
        }
        return -1;
    }

    static int Sqrt(int x) {
        if (x == 0 || x == 1) {
            return x;
        }
        double lo = 0, hi = x, mid = 0, precision = 1e-9;
        while (Math.abs(hi - lo) > precision) {
            mid = lo + ((hi - lo) / 2);
            int midSquare = (int) (mid * mid);
            if (midSquare != Integer.MAX_VALUE && midSquare == x) {
                break;
            } else if (midSquare < x) {
                lo = mid;
            } else {
                hi = mid;
            }
        }
        return (int) mid;
    }
}
