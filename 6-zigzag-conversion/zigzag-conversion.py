class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # Edge case: If 1 row or string is shorter than rows, no zigzag possible
        if numRows == 1 or numRows >= len(s):
            return s
            
        # Create an array of strings, one for each row
        rows = [""] * numRows
        cur_row = 0
        step = 1 # Start by going down
        
        for char in s:
            # Append character to the correct row's string
            rows[cur_row] += char
            
            # Check if we need to change direction
            if cur_row == 0:
                step = 1  # Hit the top, bounce down
            elif cur_row == numRows - 1:
                step = -1 # Hit the bottom, bounce up
                
            # Move cursor to the next row based on current direction
            cur_row += step
            
        # Join all the row strings together into one final string
        return "".join(rows)