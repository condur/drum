// Package search is a collection of algorithms related to searching is a collection
// e.g. Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].
package search

import (
	// "fmt"
	"math"
)

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
func Binary(x int, arr []int) int {
	idxStart, idxEnd := 0, len(arr)-1
	for idxStart <= idxEnd {
		median := (idxStart + idxEnd) / 2
		switch {
		case arr[median] == x:
			return median
		case arr[median] < x:
			idxStart = median + 1
		default:
			idxEnd = median - 1
		}
	}
	return -1
}

func sqrt(x int) int {
	// Handle edge cases
	switch x {
	case 0, 1:
		return x
	}

	const precision = 1e-5
	start, end := float64(0), float64(x)
	var median float64
	for math.Abs(end-start) > precision {
		median = (start + end) / 2
		medianSquare := int(median * median)
		if medianSquare == x {
			break
		} else if medianSquare < x {
			start = median
		} else {
			end = median
		}
	}
	return int(median)
}

//```````````````````````````````````Search Rotated Sorted Distinct`````````````````````````````````

func findPivot(nums []int) int {
	var mid int
	begin, end := 0, len(nums)-1
	for begin <= end {
		mid = begin + (end-begin)/2
		if nums[mid] >= nums[begin] && nums[mid] >= nums[end] {
			begin = mid + 1
		} else { //if nums[mid] <= nums[begin] && nums[mid] <= nums[end] {
			end = mid
		} //else {
		// 	end = mid - 1
		// }
	}
	if mid == 0 {
		return -1
	}
	return mid
}

func searchRotatedSortedDistinctArr(target int, arr []int) int {
	pivot := findPivot(arr)
	if pivot == -1 {
		return Binary(target, arr)
	} else if arr[pivot] == target {
		return pivot
	} else if x := Binary(target, arr[:pivot]); x != -1 {
		return x
	} else if x := Binary(target, arr[pivot:]); x != -1 {
		return x + pivot
	}
	return -1
}

//,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,Search Rotated Sorted Distinct,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

// Jump - find if item x exists is the array by jumping ahead by fixed steps or skipping some
// elements in place of searching all elements.
func Jump(x int, arr []int, step int) bool {
	for idx := 0; idx < len(arr); idx = idx + step {
		if x == arr[idx] {
			return true
		} else if x < arr[idx] {
			startIdx := idx - step
			if startIdx < 0 {
				startIdx = 0
			}
			for i := startIdx; i < idx; i++ {
				if x == arr[i] {
					return true
				}
			}
			break
		}
	}
	return false
}
