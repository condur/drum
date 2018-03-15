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
	// Initialize the lis array with the len of arr and set all values to 1
	var lis []int
	lis = make([]int, len(arr))
	for idx := range lis {
		lis[idx] = 1
	}

	for i := 1; i < len(arr); i++ {
		localMax := lis[i]
		for j := 0; j < i; j++ {
			if arr[j] < arr[i] {
				localMax = max(localMax, lis[j]+1)
			}
		}
		lis[i] = localMax
		maximum = max(maximum, lis[i])
	}
	return maximum
}

// MaxSumIncreasingSubSequence - solution
func MaxSumIncreasingSubSequence(arr []int) (maximum int) {
	// Initialize the msis with a copy of the arr
	msis := make([]int, len(arr))
	copy(msis, arr)

	for i := 1; i < len(arr); i++ {
		localSum := arr[i]
		for j := 0; j < i; j++ {
			if arr[j] < arr[i] {
				localSum = max(msis[j]+msis[i], msis[i])
			}
		}
		msis[i] = localSum
		maximum = max(maximum, msis[i])
	}
	return maximum
}
