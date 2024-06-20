#Task 1
submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

alice_credit = True if "Alice" in submitted and "Alice" in attended else False
print(alice_credit)