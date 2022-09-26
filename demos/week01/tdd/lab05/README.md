# Lab 05: unittest

Expand your product/ordering system API from lab #3.

## Part 1

Add unit tests (using the `unittest` library) to your existing components. Use the `unittest.mock` library to mock the components of your application so your tests remain true unit tests (isolated).

## Part 2

Add additional operations to your API:

* Add a new product to the catalog
* Edit an existing product
* Delete a product

However, for these operations, attempt to write your tests first (in TDD fashion). Practice Red/Green/Refactor as you move through the coding of this new set of operations. Ensure you use `unittest.mock` with the new operations to maintain isolation.

## Part 3

After completing parts 1 and 2, run `coverage` against your tests to assess the level of test coverage you've been able to achieve.
