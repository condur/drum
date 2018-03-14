// Package sorting is a collection of algorithms related to sorting collections
package sorting

// Selection - The selection sort algorithm sorts an array by repeatedly finding the minimum
// element (considering ascending order) from unsorted part and putting it at the beginning.
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
