package main

import (
	// "./search"
	"./sorting"
	"fmt"
)

func maxRight(arr []int) []int {
	// Initialize the result array and set the last element as -1
	var res []int
	res = make([]int, len(arr))
	res[len(arr)-1] = -1

	// Save the last element as max right side
	max := arr[len(arr)-1]

	for idx := len(arr) - 2; idx >= 0; idx-- {
		res[idx] = max
		if max < arr[idx] {
			max = arr[idx]
		}
	}
	return res
}

func main() {
	// var a, b, res uint32
	// fmt.Scanf("%v %v", &a, &b)
	// res = solveMeFirst(a, b)
	// fmt.Println(res)

	arr := []int{1, 2, 3, 4, 110, 6, 7, 8, -9}
	res := sorting.Insertion(arr)
	fmt.Println(res)
}
