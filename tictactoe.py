# Import the tkinter module
import tkinter as tk

# Create a root window
root = tk.Tk()
root.title("Tic Tac Toe")

# Create a 2D list to store the grid values
grid = [["", "", ""], ["", "", ""], ["", "", ""]]

# Create a variable to store the current player's mark
player = "X"

# Create a function to draw the grid on the window
def draw_grid():
    global grid, player
    # Loop through the grid cells
    for i in range(3):
        for j in range(3):
            # Create a button widget for each cell
            button = tk.Button(root, text=grid[i][j], font=("Arial", 32), width=5, height=2, command=lambda r=i, c=j: handle_input(r, c))
            # Place the button on the window using the grid method
            button.grid(row=i, column=j)

# Create a function to check the game state
def check_game_state():
    global grid, player
    # Check the rows for a winner
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != "":
            return player + " wins!"
    # Check the columns for a winner
    for i in range(3):
        if grid[0][i] == grid[1][i] == grid[2][i] != "":
            return player + " wins!"
    # Check the diagonals for a winner
    if grid[0][0] == grid[1][1] == grid[2][2] != "":
        return player + " wins!"
    if grid[0][2] == grid[1][1] == grid[2][0] != "":
        return player + " wins!"
    # Check if the grid is full
    if "" not in grid[0] and "" not in grid[1] and "" not in grid[2]:
        return "It's a tie!"
    # Otherwise, the game is still in progress
    return ""

# Create a function to handle the user input
def handle_input(row, column):
    global grid, player
    # Check if the cell is empty
    if grid[row][column] == "":
        # Place the mark of the current player on the cell
        grid[row][column] = player
        # Switch the player
        if player == "X":
            player = "O"
        else:
            player = "X"
        # Draw the grid on the window
        draw_grid()
        # Check the game state and display a message if the game is over
        message = check_game_state()
        if message != "":
            tk.messagebox.showinfo("Game Over", message)

# Draw the grid on the window
draw_grid()

# Run the main game loop
root.mainloop()
