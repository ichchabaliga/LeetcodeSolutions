# Last updated: 07/05/2025, 19:35:28
class Solution:
    def permute(self, numbers: List[int]) -> List[List[int]]:
    # This list will store all the possible permutations we find
        all_permutations = []

    # Helper function that builds permutations step by step
        def build_permutations(current_permutation: List[int], remaining_numbers: List[int]):
            # If there are no more numbers left to add,
            # we have a complete permutation
            if not remaining_numbers:
                all_permutations.append(current_permutation)
                return

            # Try adding each number that hasn't been used yet
            for index in range(len(remaining_numbers)):
                # Choose the next number to add
                next_number = remaining_numbers[index]
                # Create a new permutation with the chosen number added
                new_permutation = current_permutation + [next_number]
                # Create a new list of numbers without the chosen number
                new_remaining = remaining_numbers[:index] + remaining_numbers[index+1:]
                # Recursively build the rest of the permutation
                build_permutations(new_permutation, new_remaining)

        # Start with an empty permutation and all numbers available
        build_permutations([], numbers)
        return all_permutations
            