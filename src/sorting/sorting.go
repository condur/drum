// Package sorting is a collection of algorithms related to sorting collections
package sorting

// Selection - the algorithm sorts an array by repeatedly finding the minimum element
// (considering ascending order) from unsorted part and putting it at the beginning.
func Selection(arr []int) []int {
	for idx := range arr {
		for i := idx; i < len(arr); i++ {
			if arr[idx] > arr[i] {
				arr[idx], arr[i] = arr[i], arr[idx]
			}
		}
	}
	return arr
}

// Buble -  is the simplest sorting algorithm that works by repeatedly swapping
// the adjacent elements if they are in wrong order.
func Buble(arr []int) []int {
	for i := 0; i < len(arr)-1; i++ {
		swapped := false
		for j := 0; j < len(arr)-i-1; j++ {
			if arr[j] >= arr[j+1] {
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
