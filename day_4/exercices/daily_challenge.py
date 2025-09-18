import math

class Pagination:
    def __init__(self, items=None, page_size=10):
        # If no items are provided, use an empty list
        self.items = items if items is not None else []
        self.page_size = int(page_size)   # ensure it's an integer
        self.current_idx = 0  # page index (0-based)
        self.total_pages = math.ceil(len(self.items) / self.page_size) if self.page_size > 0 else 0

    def get_visible_items(self):
        """Return the list of items visible on the current page."""
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    # ---- Navigation Methods ---- #
    def go_to_page(self, page_num):
        """Go to a specific page (1-based)."""
        if page_num < 1 or page_num > self.total_pages:
            raise ValueError(f"Page {page_num} is out of range. Must be between 1 and {self.total_pages}.")
        self.current_idx = page_num - 1

    def first_page(self):
        self.current_idx = 0
        return self  # allow method chaining

    def last_page(self):
        self.current_idx = self.total_pages - 1 if self.total_pages > 0 else 0
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        """Return items of current page as a string, one per line."""
        return "\n".join(str(item) for item in self.get_visible_items())


# ------------------ TEST CASES ------------------ #
alphabetList = list("abcdefghijklmnopqrstuvwxyz")
p = Pagination(alphabetList, 4)

print(p.get_visible_items())
# ['a', 'b', 'c', 'd']

p.next_page()
print(p.get_visible_items())
# ['e', 'f', 'g', 'h']

p.last_page()
print(p.get_visible_items())
# ['y', 'z']

p.go_to_page(7)
print(p.current_idx + 1)
# Output: 7

try:
    p.go_to_page(0)
except ValueError as e:
    print("Error:", e)
