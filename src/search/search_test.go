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
		want bool
	}{
		{[]int{1, 2, 3, 4, 5}, 2, true},
		{[]int{1, 2, 3, 4, 5}, 10000, false},
	}
	for _, table := range tables {
		got := Binary(table.x, table.arr)
		if got != table.want {
			t.Errorf("Binary search of %d was incorrect, got: %t, want: %t.", table.x, got, table.want)
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
