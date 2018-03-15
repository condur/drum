package dynamic

func min(x, y int) int {
	if x < y {
		return x
	}
	return y
}

func max(x, y int) int {
	if x > y {
		return x
	}
	return y
}

// LongestIncreasingSubsequence - solution for the problem
func LongestIncreasingSubsequence(arr []int) (maximum int) {
	// Initialize the lis array
	var lis []int
	lis = make([]int, len(arr))

	for i := 1; i < len(arr); i++ {
		localMax, found := 0, false
		for j := i - 1; j >= 0; j-- {
			if arr[j] < arr[i] {
				localMax = max(localMax, lis[j])
				found = true
			}
		}
		if found == true {
			lis[i] = localMax + 1
			maximum = max(maximum, lis[i])
		}
	}
	return maximum + 1
}
