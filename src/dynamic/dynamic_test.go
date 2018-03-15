package dynamic

import "testing"

func TestMin(t *testing.T) {
	tables := []struct {
		x   int
		y   int
		res int
	}{
		{1, 1, 1},
		{1, 2, 1},
		{0, 2, 0},
		{-1, 2, -1},
	}
	for _, table := range tables {
		minimum := min(table.x, table.y)
		if minimum != table.res {
			t.Errorf("Min of (%d, %d) was incorrect, got: %d, want: %d.", table.x, table.y, minimum, table.res)
		}
	}
}

func TestMax(t *testing.T) {
	tables := []struct {
		x   int
		y   int
		res int
	}{
		{1, 1, 1},
		{1, 2, 2},
		{0, 2, 2},
		{-1, 2, 2},
	}
	for _, table := range tables {
		maximum := max(table.x, table.y)
		if maximum != table.res {
			t.Errorf("Maxß of (%d, %d) was incorrect, got: %d, want: %d.", table.x, table.y, maximum, table.res)
		}
	}
}

func TestLIS(t *testing.T) {
	arr := []int{10, 22, 9, 33, 21, 50, 41, 60, 80}
	want := 6
	got := LongestIncreasingSubsequence(arr)

	if got != want {
		t.Errorf("Longest Increasing Subsequence is incorrect, got: %d, want: %d.", got, want)
	}
}
