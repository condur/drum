package search

import "testing"

func TestLinear(t *testing.T) {
	tables := []struct {
		arr  []int
		x    int
		want int
	}{
		{[]int{1, 101, 2, 3, 100, 4, 5}, 2, 2},
		{[]int{1, 101, 2, 3, 100, 4, 5}, 10000, -1},
	}
	for _, table := range tables {
		got := Linear(table.x, table.arr)
		if got != table.want {
			t.Errorf("Linear search of %d was incorrect, got: %d, want: %d.", table.x, got, table.want)
		}
	}
}

func TestBinary(t *testing.T) {
	tables := []struct {
		arr  []int
		x    int
		want int
	}{
		{[]int{1, 2, 3, 4, 5}, 2, 1},
		{[]int{1, 2, 3, 4, 5, 6}, 6, 5},
		{[]int{1, 2, 3, 4, 5}, 10000, -1},
	}
	for _, table := range tables {
		got := Binary(table.x, table.arr)
		if got != table.want {
			t.Errorf("Binary search of %d was incorrect, got: %d, want: %d.", table.x, got, table.want)
		}
	}
}

func TestBinaryV2(t *testing.T) {
	tables := []struct {
		arr  []int
		x    int
		want int
	}{
		{[]int{1, 2, 3, 4, 5}, 2, 1},
		{[]int{1, 2, 3, 4, 5}, 5, 4},
		{[]int{1, 2, 3, 4, 5, 6}, 6, 5},
		{[]int{1, 2, 3, 4, 5}, 10000, -1},
	}
	for _, table := range tables {
		got := binaryV2(table.arr, table.x)
		if got != table.want {
			t.Errorf("Binary search of %d was incorrect, got: %d, want: %d.", table.x, got, table.want)
		}
	}
}

func TestJump(t *testing.T) {
	tables := []struct {
		arr  []int
		x    int
		want bool
	}{
		{[]int{1, 2, 3, 4, 5}, 2, true},
		{[]int{1, 2, 3, 4, 5}, 3, true},
		{[]int{1, 2, 3, 4, 5}, 10000, false},
		{[]int{1, 2, 3, 4, 5}, -10000, false},
	}
	for _, table := range tables {
		got := Jump(table.x, table.arr, 2)
		if got != table.want {
			t.Errorf("Jump search of %d was incorrect, got: %t, want: %t.", table.x, got, table.want)
		}
	}
}

func TestSQRT(t *testing.T) {
	tables := []struct {
		x    int
		want int
	}{
		{8, 2},
		{4, 2},
		{1, 1},
	}
	for _, table := range tables {
		got := sqrt(table.x)
		if got != table.want {
			t.Errorf("SQRT of %d was incorrect, got: %d, want: %d.", table.x, got, table.want)
		}
	}
}

func TestFindPivot(t *testing.T) {
	tables := []struct {
		arr  []int
		want int
	}{
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 6},
		{[]int{8, 9, 1, 2, 4, 5, 6, 7}, 2},
		{[]int{4, 5, 6, 7, 0, 1, 2}, 4},
		{[]int{4, 5, 6, 7, 0}, 4},
		{[]int{4, 5, 6, 7, 8, 9}, -1},
		{[]int{}, -1},
		{[]int{1}, -1},
		{[]int{1, 0}, 1},
		{[]int{1, 2}, -1},
		{[]int{3, 0, 1}, 1},
	}
	for _, table := range tables {
		got := findPivot(table.arr)
		if got != table.want {
			t.Errorf("Find pivot search was incorrect, got: %d, want: %d.", got, table.want)
		}
	}
}

func TestSearchRotatedSortedDistinctArr(t *testing.T) {
	tables := []struct {
		arr  []int
		x    int
		want int
	}{
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 1, 6},
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 10, -1},
		{[]int{4, 5, 6, 7, 8, 9}, 10, -1},
		{[]int{4, 5, 6, 7, 8, 9}, 9, 5},
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 2, 7},
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 9, 5},
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 4, 0},
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 6, 2},
		{[]int{8, 9, 1, 2, 4, 5, 6, 7}, 2, 3},
		{[]int{4, 5, 6, 7, 0, 1, 2}, 4, 0},
		{[]int{4, 5, 6, 7, 0}, 4, 0},
		{[]int{4, 5, 6, 7, 8, 9}, 5, 1},
		{[]int{}, -1, -1},
		{[]int{1}, -1, -1},
		{[]int{1, 0}, 1, 0},
		{[]int{1, 2}, -1, -1},
		{[]int{3, 0, 1}, 1, 2},
	}
	for _, table := range tables {
		got := searchRotatedSortedDistinctArr(table.x, table.arr)
		if got != table.want {
			t.Errorf("Rotated Sorted Distinct array search of %d was incorrect, got: %d, want: %d.", table.x, got, table.want)
		}
	}
}

func TestFindPeek(t *testing.T) {
	tables := []struct {
		arr  []int
		want int
	}{
		{[]int{4, 5, 6, 7, 8, 9, 1, 2}, 5},
		{[]int{8, 9, 1, 2, 4, 5, 6, 7}, 7},
		{[]int{4, 5, 6, 7, 0, 1, 2}, 3},
		{[]int{4, 5, 6, 7, 0}, 3},
		{[]int{4, 5, 6, 7, 8, 9}, 5},
		{[]int{}, -1},
		{[]int{1}, 0},
		{[]int{1, 0}, 0},
		{[]int{1, 2}, 1},
		{[]int{3, 0, 1}, 0},
	}
	for _, table := range tables {
		got := findPeakElement(table.arr)
		if got != table.want {
			t.Errorf("Find pivot search was incorrect, got: %d, want: %d.", got, table.want)
		}
	}
}
