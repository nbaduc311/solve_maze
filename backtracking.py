# Mê cung là một ma trận 2D với 1 là đường có thể đi, 0 là vật cản.
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

N = len(maze)  # Kích thước mê cung

# Hàm kiểm tra xem vị trí có hợp lệ để di chuyển không
def isSafe(maze, x, y):
    if 0 <= x < N and 0 <= y < N and maze[x][y] == 1:
        return True
    return False

# Hàm giải mê cung bằng Backtracking
def solveMaze(maze):
    # Tạo ma trận kết quả ban đầu với toàn số 0
    sol = [[0 for _ in range(N)] for _ in range(N)]

    # Gọi hàm đệ quy để bắt đầu từ vị trí (0,0)
    if solveMazeUtil(maze, 0, 0, sol) == False:
        print("Không tìm được đường đi")
        return False

    # In ra đường đi
    printSolution(sol)
    return True

# Hàm đệ quy để tìm đường đi
def solveMazeUtil(maze, x, y, sol):
    # Nếu đến được đích, đánh dấu vị trí và trả về True
    if x == N-1 and y == N-1:
        sol[x][y] = 1
        return True

    # Kiểm tra xem có thể di chuyển tới vị trí (x, y) hay không
    if isSafe(maze, x, y):
        # Đánh dấu vị trí này là một phần của đường đi
        sol[x][y] = 1

        # Di chuyển xuống dưới
        if solveMazeUtil(maze, x+1, y, sol):
            return True

        # Di chuyển sang phải
        if solveMazeUtil(maze, x, y+1, sol):
            return True
        # Di chuyển sang trái
        if solveMazeUtil(maze, x, y-1, sol):
            return True


        # Di chuyển lên trên
        if solveMazeUtil(maze, x-1, y, sol):
            return True


        # Nếu không tìm được đường, hủy đánh dấu (Backtrack)
        sol[x][y] = 0
        return False

    return False

# Hàm in ma trận kết quả
def printSolution(sol):
    for i in sol:
        print(i)

# Gọi hàm giải mê cung
solveMaze(maze)
