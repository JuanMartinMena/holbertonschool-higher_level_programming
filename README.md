### Lists (`list`)

- **Definition:** Lists are ordered and mutable collections of elements. They are defined using square brackets `[]`.
- **Characteristics:**
    - **Mutable:** You can modify their elements (add, remove, or change items).
    - **Mixed data types:** They can contain elements of different data types.
    - **Indexing:** Elements can be accessed using indices (positive or negative).
    - **Slicing:** You can obtain sublists using slicing (`list[start:stop]`).
- **Common Methods:**
    - `append(x)`: Adds an element `x` to the end of the list.
    - `insert(i, x)`: Inserts an element `x` at position `i`.
    - `remove(x)`: Removes the first occurrence of the element `x`.
    - `pop(i)`: Removes and returns the element at position `i`.
    - `sort()`: Sorts the list in ascending order.
    - `reverse()`: Reverses the order of the list.
    - `len()`: Returns the length of the list.

### Tuples (`tuple`)

- **Definition:** Tuples are ordered and immutable collections of elements. They are defined using parentheses `()`.
- **Characteristics:**
    - **Immutable:** They cannot be modified after creation.
    - **Mixed data types:** They can contain elements of different data types.
    - **Indexing and Slicing:** Similar to lists, you can access and obtain sub-tuples.
- **Usage:** Ideal for data that should not change over time, such as coordinates (x, y) or days of the week.
- **Common Methods:**
    - `count(x)`: Returns the number of times `x` appears in the tuple.
    - `index(x)`: Returns the first position of `x` in the tuple.
    - **Note:** There are no methods like `append()` or `remove()` since tuples are immutable.

### Key Differences Between Lists and Tuples:

- **Mutability:** Lists are mutable, tuples are not.
- **Performance:** Tuples can be faster and use less memory than lists due to their immutability.
- **Usage:** Lists are used for collections of data that may change, while tuples are used for fixed data.

### Example of Usage:

- **List:** Used for a to-do list where you can add or remove items.
- **Tuple:** Used for representing a date (year, month, day) that doesn’t change.
