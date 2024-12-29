from typing import List

class Letter:
    def __init__(self, letter: str, row: int, column: int):
        self.rc = (row, column)
        self._letter = letter

    def __str__(self):
        return f"{self._letter}"

    def __repr__(self):
        return f"Letter: {self._letter}, Row: {self.rc[0]}, Column: {self.rc[1]}"


def read_input(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def create_grid(input_data: List[str]) -> List[List[Letter]]:
    return [[Letter(char, row, col) for col, char in enumerate(line)] for row, line in enumerate(input_data)]

def check_horizontal(grid: List[List[Letter]], word: str) -> int:
    matches = 0
    for row in grid:
        row_letters = ''.join([letter._letter for letter in row])
        if word in row_letters:
            matches += row_letters.count(word)
        if word[::-1] in row_letters:
            matches += row_letters.count(word[::-1])
    return matches

def check_vertical(grid: List[List[Letter]], word: str) -> int:
    matches = 0
    columns = len(grid[0])
    for col in range(columns):
        column_letters = ''.join([grid[row][col]._letter for row in range(len(grid))])
        if word in column_letters:
            matches += column_letters.count(word)
        if word[::-1] in column_letters:
            matches += column_letters.count(word[::-1])
    return matches

def check_diagonal(grid: List[List[Letter]], word: str) -> int:
    matches = 0
    rows, cols = len(grid), len(grid[0])

    # Check diagonals: top-left to bottom-right
    for start_row in range(rows):
        diagonal = ''.join([grid[start_row + i][i]._letter for i in range(min(rows - start_row, cols))])
        if word in diagonal:
            matches += diagonal.count(word)
        if word[::-1] in diagonal:
            matches += diagonal.count(word[::-1])

    for start_col in range(1, cols):
        diagonal = ''.join([grid[i][start_col + i]._letter for i in range(min(rows, cols - start_col))])
        if word in diagonal:
            matches += diagonal.count(word)
        if word[::-1] in diagonal:
            matches += diagonal.count(word[::-1])

    # Check diagonals: top-right to bottom-left
    for start_row in range(rows):
        diagonal = ''.join([grid[start_row + i][cols - 1 - i]._letter for i in range(min(rows - start_row, cols))])
        if word in diagonal:
            matches += diagonal.count(word)
        if word[::-1] in diagonal:
            matches += diagonal.count(word[::-1])

    for start_col in range(1, cols):
        diagonal = ''.join([grid[i][cols - 1 - start_col - i]._letter for i in range(min(rows, cols - start_col))])
        if word in diagonal:
            matches += diagonal.count(word)
        if word[::-1] in diagonal:
            matches += diagonal.count(word[::-1])

    return matches

def main():
    file_path = 'input/4.txt'
    word_to_search = "XMAS"

    input_data = read_input(file_path)
    grid = create_grid(input_data)

    for row in grid:
        print(' '.join(str(letter) for letter in row))

    # Check matches
    horizontal_matches = check_horizontal(grid, word_to_search)
    vertical_matches = check_vertical(grid, word_to_search)
    diagonal_matches = check_diagonal(grid, word_to_search)

    total_matches = horizontal_matches + vertical_matches + diagonal_matches

    print(f"Horizontal Matches: {horizontal_matches}")
    print(f"Vertical Matches: {vertical_matches}")
    print(f"Diagonal Matches: {diagonal_matches}")
    print(f"Total Matches: {total_matches}")

if __name__ == "__main__":
    main()
