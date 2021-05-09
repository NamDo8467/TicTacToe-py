def check_horizontal():
    row = 0
    row1 = 1
    row2 = 2

    col = 0
    col1 = 1
    col2 = 2
    if grid[row][col] == grid[row][col1] == grid[row][col2] == 'x':
        return 'x'
    elif grid[row][col] == grid[row][col1] == grid[row][col2] == 'o':
        return 'o'
    elif grid[row1][col] == grid[row1][col1] == grid[row1][col2] == 'x':
        return 'x'
    elif grid[row1][col] == grid[row1][col1] == grid[row1][col2] == 'o':
        return 'o'
    elif grid[row2][col] == grid[row2][col1] == grid[row2][col2] == 'x':
        return 'x'
    elif grid[row2][col] == grid[row2][col1] == grid[row2][col2] == 'o':
        return 'o'


def check_vertical():
    row = 0
    row1 = 1
    row2 = 2

    col = 0
    col1 = 1
    col2 = 2
    if grid[row][col] == grid[row1][col] == grid[row2][col] == 'x':
        return 'x'
    elif grid[row][col] == grid[row1][col] == grid[row2][col] == 'o':
        return 'o'
    elif grid[row][col1] == grid[row1][col1] == grid[row2][col1] == 'x':
        return 'x'
    elif grid[row][col1] == grid[row1][col1] == grid[row2][col1] == '0':
        return 'o'
    elif grid[row][col2] == grid[row1][col2] == grid[row2][col2] == 'x':
        return 'x'
    elif grid[row][col2] == grid[row1][col2] == grid[row2][col2] == 'o':
        return 'o'


def check_diagonal():
    row = 0
    row1 = 1
    row2 = 2
    col = 0
    col1 = 1
    col2 = 2
    if grid[row][col] == grid[row1][col1] == grid[row2][col2] == 'x':
        return 'x'
    elif grid[row][col] == grid[row1][col1] == grid[row2][col2] == 'o':
        return 'o'
    elif grid[row][col2] == grid[row1][col1] == grid[row2][col] == 'x':
        return 'x'
    elif grid[row][col2] == grid[row1][col1] == grid[row2][col] == 'o':
        return 'o'


def place_x():
    x_position = input("At which position do you want to place an 'x': ")

    if int(x_position) == 1 or int(x_position) == 2 or int(x_position) == 3:
        grid[0][int(x_position) - 1] = 'x'
        for i in range(0, grid.__len__()):
            for j in range(0, grid.__len__()):
                print(grid[i][j], end=" ")
            print()

    if int(x_position) == 4 or int(x_position) == 5 or int(x_position) == 6:
        if int(x_position) == 4:
            grid[1][0] = 'x'
        elif int(x_position) == 5:
            grid[1][1] = 'x'
        elif int(x_position) == 6:
            grid[1][2] = 'x'
        for i in range(0, grid.__len__()):
            for j in range(0, grid.__len__()):
                print(grid[i][j], end=" ")
            print()

    if int(x_position) == 7 or int(x_position) == 8 or int(x_position) == 9:
        if int(x_position) == 7:
            grid[2][0] = 'x'
        elif int(x_position) == 8:
            grid[2][1] = 'x'
        elif int(x_position) == 9:
            grid[2][2] = 'x'
        for i in range(0, grid.__len__()):
            for j in range(0, grid.__len__()):
                print(grid[i][j], end=" ")
            print()


def place_0():
    o_position = input("At which position do you want to place an 'o': ")

    if int(o_position) == 1 or int(o_position) == 2 or int(o_position) == 3:
        grid[0][int(o_position) - 1] = 'o'
        for i in range(0, grid.__len__()):
            for j in range(0, grid.__len__()):
                print(grid[i][j], end=" ")
            print()

    if int(o_position) == 4 or int(o_position) == 5 or int(o_position) == 6:
        if int(o_position) == 4:
            grid[1][0] = 'o'
        elif int(o_position) == 5:
            grid[1][1] = 'o'
        elif int(o_position) == 6:
            grid[1][2] = 'o'
        for i in range(0, grid.__len__()):
            for j in range(0, grid.__len__()):
                print(grid[i][j], end=" ")
            print()

    if int(o_position) == 7 or int(o_position) == 8 or int(o_position) == 9:
        if int(o_position) == 7:
            grid[2][0] = 'o'
        elif int(o_position) == 8:
            grid[2][1] = 'o'
        elif int(o_position) == 9:
            grid[2][2] = 'o'
        for i in range(0, grid.__len__()):
            for j in range(0, grid.__len__()):
                print(grid[i][j], end=" ")
            print()


count = 0
grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(0, grid.__len__()):
    for j in range(0, grid.__len__()):
        print(grid[i][j], end=" ")
    print()
while count != 9:
    place_0()
    count += 1
    if count >= 9:break
    if check_horizontal() == 'x' or check_diagonal() == 'x' or check_vertical() == 'x':
        print('X player won')
        break

    if check_horizontal() == 'o' or check_diagonal() == 'o' or check_vertical() == 'o':
        print('O player won')
        break
    place_x()
    count += 1
    if count >= 9:break
    if check_horizontal() == 'x' or check_diagonal() == 'x' or check_vertical() == 'x':
        print('X player won')
        break

    if check_horizontal() == 'o' or check_diagonal() == 'o' or check_vertical() == 'o':
        print('O player won')
        break
    
