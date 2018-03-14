// Package search is a collection of algorithms related to searching is a collection
// e.g. Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
package search

// Linear - find if item x exists is the array, return the index of the item or -1
func Linear(x int, arr []int) int {
	for idx, item := range arr {
		if x == item {
			return idx
		}
	}
	return -1
}

// Binary - find if item x exists is the array, return if the item exists or not
func Binary(x int, arr []int) bool {
	idxStart := 0
	idxEnd := len(arr) - 1

	for idxStart <= idxEnd {
		median := (idxStart + idxEnd) / 2
		switch {
		case arr[median] == x:
			return true
		case arr[median] < x:
			idxStart = median + 1
		default:
			idxEnd = median - 1
		}
	}
	return false
}

// Jump - find if item x exists is the array by jumping ahead by fixed steps or skipping some
// elements in place of searching all elements.
func Jump(x int, arr []int, step int) bool {
	for idx := 0; idx < len(arr); idx = idx + step {
		switch {
		case x == arr[idx]:
			return true
		case x < arr[idx]:
			startIdx := idx - step
			if startIdx < 0 {
				startIdx = 0
			}
			for i := startIdx; i < idx; i++ {
				if x == arr[i] {
					return true
				}
			}
		}
	}
	return false
}
