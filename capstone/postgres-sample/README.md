# unittest with Mocks

Using the provided starting point, build a product/ordering system API in Python using FastAPI. Include the following models within that API:

* Product Structure
    - Internal ID (auto-increment)
    - Product number (e.g., "ABC-123")
    - Product description
    - Unit cost
* Order Structure
    - Internal ID (auto-increment)
    - Product ID (foreign key)
    - Order number (e.g., "12345")
    - Quantity
    - Total
* Operations to Include
    - List all products in the catalog
    - List a specific product in the catalog by product number
    - Accept a new order for a single product
    - Retrieve a specific order's details by order number

Use the provided SQLite database (code in the `start` folder can be used to create the database automatically) as a starting point for persisting your catalog and order information. The starting point for the lab has sample data preloaded with a set of products.

You'll be seeking to build the components of your API in a loosely-coupled manner, layer components in modules correctly, etc. such that the components of your API are clean and well architected. For example, whatever storage/persistence strategy you use, the rest of the API should not need to know or care. Ensure that functionality is sufficiently isolated to modules and that each module is insulated from the others (to prevent brittle coupling).

## Part 1

Build the set of features outlined above using TDD and include unit tests using the `unittest` library. Use the `unittest.mock` library to mock the components of your application so your tests remain true unit tests (isolated).

## Part 2

Add additional operations to your API:

* Add a new product to the catalog
* Edit an existing product

As with the previous, use TDD and `unittest` to build a corresponding set of automated tests to accompany the production code. Practice Red/Green/Refactor as you move through the coding of this new set of operations. Ensure you use `unittest.mock` with the new operations to maintain isolation.

## Part 3

After completing parts 1 and 2, run `coverage` against your tests to assess the level of test coverage you've been able to achieve.
