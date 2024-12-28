from typing import List

def read_input(file_path: str) -> List[str]:
    """Reads the input file and returns a list of report strings."""
    with open(file_path, 'r') as file:
        return file.read().strip().split('\n')

def is_safe(levels: List[int]) -> bool:
    """Checks if the levels are either all increasing or all decreasing with differences between 1 and 3."""
    if len(levels) < 2:
        return True

    trend = 1 if levels[0] < levels[1] else -1

    for i in range(len(levels) - 1):
        current_level = levels[i]
        next_level = levels[i + 1]

        if (current_level > next_level and trend == 1) or (current_level < next_level and trend == -1):
            return False

        if not (1 <= abs(current_level - next_level) <= 3):
            return False

    return True

def check_level(levels: List[int], dampener: int = 1) -> bool:
    """Checks if the levels are safe, considering the Problem Dampener."""
    if is_safe(levels):
        return True

    if dampener == 0:
        return False

    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i+1:]
        if is_safe(modified_levels):
            return True

    return False

def analyze_reports(reports: List[str]) -> int:
    """Analyzes the reports and counts the number of safe levels."""
    safe_report_count = 0
    for report in reports:
        if report.strip():  # Ensure we don't process empty lines
            levels = list(map(int, report.split()))
            if check_level(levels):
                safe_report_count += 1
    return safe_report_count

if __name__ == "__main__":
    reports = read_input('input/2.txt')
    number_of_safe_levels = analyze_reports(reports)
    print(f'Number of safe levels: {number_of_safe_levels}')
