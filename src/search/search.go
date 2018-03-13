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

// Binary - find if item x exists is the array, return the index of the item or -1
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
