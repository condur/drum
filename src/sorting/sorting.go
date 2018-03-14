// Package sorting is a collection of algorithms related to sorting collections
package sorting

// Find the min item and its index in the array
func min(arr []int, startIdx int) (minIdx int, min int) {
	minIdx, min = startIdx, arr[startIdx]
	for idx := startIdx; idx < len(arr); idx++ {
		if min > arr[idx] {
			minIdx, min = idx, arr[idx]
		}
	}
	return minIdx, min
}

// Selection - the algorithm sorts an array by repeatedly finding the minimum element
// (considering ascending order) from unsorted part and putting it at the beginning.
func Selection(arr []int) []int {
	for idx := range arr {
		minIdx, _ := min(arr, idx)
		arr[idx], arr[minIdx] = arr[minIdx], arr[idx]
	}
	return arr
}

// Buble -  is the simplest sorting algorithm that works by repeatedly swapping
// the adjacent elements if they are in wrong order.
func Buble(arr []int) []int {
	for i := 0; i < len(arr)-1; i++ {
		swapped := false
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapped = true
			}
		}
		if swapped == false {
			break
		}
	}
	return arr
}

// Insertion - is a simple sorting algorithm that builds the final sorted array one item at a time.
func Insertion(arr []int) []int {
	var key int
	for i := 1; i < len(arr); i++ {
		key = arr[i]
		j := i - 1
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			j--
		}
		arr[j+1] = key
	}
	return arr
}
