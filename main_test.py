# package main
#
# import (
# 	"testing"
# )
#
# func TestHeuristicManhattan(t *testing.T) {
# 	// Test input
# 	state := State{
# 		board: [3][3]int{
# 			{1, 2, 3},
# 			{4, 5, 6},
# 			{7, 8, 0},
# 		},
# 		zeroX: 2,
# 		zeroY: 2,
# 	}
#
# 	// Expected output
# 	expected := 0 // Since this is already the goal state
#
# 	// Call the function
# 	result := HeuristicManhattan(&state)
#
# 	// Assert the result
# 	if result != expected {
# 		t.Errorf("HeuristicManhattan was incorrect, got: %d, want: %d.", result, expected)
# 	}
# }
#
# func TestExpand(t *testing.T) {
# 	// Initial state near the goal
# 	state := State{
# 		board: [3][3]int{
# 			{1, 2, 3},
# 			{4, 5, 6},
# 			{7, 0, 8},
# 		},
# 		zeroX: 2,
# 		zeroY: 1,
# 		cost:  0,
# 	}
#
# 	// We expect 4 possible moves
# 	expectedNumMoves := 4
#
# 	// Call the function
# 	results := Expand(&state)
#
# 	// Check the number of results
# 	if len(results) != expectedNumMoves {
# 		t.Errorf("Expand returned %d states, expected %d", len(results), expectedNumMoves)
# 	}
# }
#
# func TestFindZero(t *testing.T) {
# 	// Setup the board
# 	board := [3][3]int{
# 		{1, 2, 3},
# 		{4, 5, 6},
# 		{7, 8, 0},
# 	}
# 	expectedX, expectedY := 2, 2
#
# 	// Execution
# 	x, y := FindZero(board)
#
# 	// Assertion
# 	if x != expectedX || y != expectedY {
# 		t.Errorf("FindZero was incorrect, got: (%d, %d), want: (%d, %d).", x, y, expectedX, expectedY)
# 	}
# }
