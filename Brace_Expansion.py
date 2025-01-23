class Solution:
    def expand(self, s: str) -> List[str]:
        """
        Approach:
        - Parse the input string to identify groups of options (delimited by curly braces) or fixed characters.
        - Use backtracking to generate all possible combinations of words.
        - Sort the resulting combinations in lexicographical order and return them.
        Time Complexity: 
        - O(k^n * n log n), where k is the maximum size of a group, and n is the number of groups.
        - Generating all combinations takes O(k^n), and sorting takes O(n log n).
        Space Complexity:
        - O(k^n), for storing all combinations.
        """

        def parse_string(s: str) -> List[List[str]]:
            """
            Parses the input string into a list of options for each position.
            Each position is either a list of characters (for braces) or a single character.
            """
            parsed = []
            i = 0
            while i < len(s):
                if s[i] == '{':
                    # Extract characters inside braces
                    j = i + 1
                    while s[j] != '}':
                        j += 1
                    parsed.append(sorted(s[i+1:j].split(',')))  # Add sorted options
                    i = j + 1  # Move past the closing brace
                else:
                    # Add single character
                    parsed.append([s[i]])
                    i += 1
            return parsed

        def backtrack(index: int, path: List[str]):
            """
            Backtracking to generate all combinations.
            """
            # If we've processed all groups, add the current combination to results
            if index == len(parsed):
                results.append("".join(path))
                return

            # Iterate through all options in the current group
            for char in parsed[index]:
                path.append(char)  # Choose
                backtrack(index + 1, path)  # Recurse
                path.pop()  # Undo choice

        # Parse the string into groups
        parsed = parse_string(s)

        # Initialize results list and perform backtracking
        results = []
        backtrack(0, [])
        return results
