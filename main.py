import heapq
import time

class State:
    def __init__(self, board, zeroX, zeroY, cost, heuristic, prev):
        self.board = board
        self.zeroX = zeroX
        self.zeroY = zeroY
        self.cost = cost
        self.heuristic = heuristic
        self.prev = prev

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

    def __eq__(self, other):
        return (self.cost + self.heuristic) == (other.cost + other.heuristic)

solution = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

def readRow(rowNum):
    input_str = input()
    numbers = [int(num) for num in input_str.split(",")]
    if len(numbers) != 3:
        raise ValueError("invalid input: must contain 3 numbers separated by commas")
    return numbers

def heuristic_simple(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0 and state.board[i][j] != solution[i][j]:
                count += 1
    return count

def heuristic_manhattan(state):
    target_pos = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                  4: (1, 0), 5: (1, 1), 6: (1, 2),
                  7: (2, 0), 8: (2, 1), 0: (2, 2)}
    sum = 0
    for i in range(3):
        for j in range(3):
            value = state.board[i][j]
            if value != 0:
                target = target_pos[value]
                sum += abs(target[0] - i) + abs(target[1] - j)
    return sum


def find_zero(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j
    return -1, -1  # this should never happen if input is correct

def expand(current):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    states = []
    print("Expanding states...")
    for d in directions:
        nx, ny = current.zeroX + d[0], current.zeroY + d[1]
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_board = [row[:] for row in current.board]  # Copy the board
            new_board[current.zeroX][current.zeroY], new_board[nx][ny] = new_board[nx][ny], new_board[current.zeroX][current.zeroY]
            new_state = State(new_board, nx, ny, current.cost + 1, 0, current)
            states.append(new_state)
    return states

def main():
    board = []
    print("Enter each row separately. 0 represents the empty space.")
    print("Enter the first row of the puzzle board, separate by commas (e.g., 1,2,3)")
    board.append(readRow(0))
    print("Enter the second row of the puzzle board:")
    board.append(readRow(1))
    print("Enter the third row of the puzzle board:")
    board.append(readRow(2))

    # Now you have the board assembled in the 'board' list
    print("Board:")
    for row in board:
        print(" ".join(map(str, row)))

    if not solvable(board, solution):
        print("No solution exists")
        return

    zeroX, zeroY = find_zero(board)
    print(f"Zero found at ({zeroX}, {zeroY})")

    start_state = State(board, zeroX, zeroY, 0, 0, None)

    print("Choose the search algorithm: 1 for Uniform Cost, 2 for A* Simple, 3 for A* Precise")
    choice = int(input())

    heuristic_func = None
    if choice == 1:
        heuristic_func = lambda s: 0  # Uniform Cost Search
    elif choice == 2:
        heuristic_func = heuristic_simple
    elif choice == 3:
        heuristic_func = heuristic_manhattan
    else:
        print("Invalid choice.")
        return

    start_state.heuristic = heuristic_func(start_state)
    pq = [start_state]

    nodes_visited = 0
    start_time = time.time()

    while pq:
        current = heapq.heappop(pq)
        nodes_visited += 1

        print(f"Visiting node with heuristic {current.heuristic} and cost {current.cost}")

        if current.board == solution:  # Check if this is the goal state
            duration = time.time() - start_time
            print("Solution path:")
            print_solution(current)
            print(f"Nodes visited: {nodes_visited}")
            print(f"Path length: {current.cost}")
            print(f"Execution time: {duration} seconds")
            return

        for next_state in expand(current):
            next_state.heuristic = heuristic_func(next_state)
            heapq.heappush(pq, next_state)

    print("No solution found")

def print_solution(state):
    if state.prev is not None:
        print_solution(state.prev)
    print(state.board)

def solvable(board, goal):
    inv_goal = 0
    board_array = [board[i][j] for i in range(3) for j in range(3)]
    goal_array = [goal[i][j] for i in range(3) for j in range(3)]

    for i in range(len(goal_array)):
        for j in range(i + 1, len(goal_array)):
            if goal_array[i] > goal_array[j] and goal_array[j] != 0:
                inv_goal += 1

    inv_board = 0
    for i in range(len(board_array)):
        for j in range(i + 1, len(board_array)):
            if board_array[i] > board_array[j] and board_array[j] != 0:
                inv_board += 1

    return inv_goal % 2 == inv_board % 2

if __name__ == "__main__":
    main()
