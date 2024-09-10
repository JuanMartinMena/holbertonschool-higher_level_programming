### Lists (`list`)

- **Definition:** Lists are ordered and mutable collections of elements. They are defined using square brackets `[]`.
- **Characteristics:**
    - **Mutable:** You can modify its elements (add, remove, or change).
    - **Mixed Data Types:** Can contain elements of different data types.
    - **Indexing:** Elements can be accessed using indices (both positive and negative).
    - **Slicing:** You can obtain sublists using slicing (`list[start:stop]`).
- **Common Methods:**
    - `append(x)`: Adds an element `x` to the end of the list.
    - `insert(i, x)`: Inserts an element `x` at position `i`.
    - `remove(x)`: Removes the first occurrence of element `x`.
    - `pop(i)`: Removes and returns the element at position `i`.
    - `sort()`: Sorts the list in ascending order.
    - `reversed()`: Reverses the order of the list.
    - `len()`: Returns the length of the list.
    - `.copy()`: Creates a new instance of the object, but the internal elements (if they are mutable objects) are still referenced from the original object. Changes to these internal elements will be reflected in both the copy and the original.
    - `deepcopy()`: To create a complete copy that includes independent copies of the internal objects, you can use the `copy` module and the `deepcopy()` function. This is useful if you need an independent copy where changes to the new object do not affect the original or its internal elements.
    - `join()`: **`''.join(new_string)`**: Joins all characters in `new_string` into a single string with no separator between them.


---

### Tuples (`tuple`)

- **Definition:** Tuples are ordered and immutable collections of elements. They are defined using parentheses `()`.
- **Characteristics:**
    - **Immutable:** Cannot be modified after creation.
    - **Mixed Data Types:** Can contain elements of different data types.
    - **Indexing and Slicing:** Similar to lists, you can access and obtain sub-tuples.
- **Usage:** Ideal for data that should not change over time, such as coordinates (x, y) or days of the week.
- **Common Methods:**
    - `count(x)`: Returns the number of times `x` appears in the tuple.
    - `index(x)`: Returns the first position of `x` in the tuple.
    - **Note:** No methods like `append()` or `remove()` since tuples are immutable.

### Key Differences Between Lists and Tuples:

- **Mutability:** Lists are mutable, tuples are not.
- **Performance:** Tuples may be faster and use less memory than lists due to their immutability.
- **Usage:** Lists are used for collections of data that may change, while tuples are used for fixed data.

### Example Usage:

- **List:** Used for a to-do list where you can add or remove items.
- **Tuple:** Used to represent a date (year, month, day) which should not change.
