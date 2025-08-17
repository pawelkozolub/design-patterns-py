# General
Examples of design patterns in Python.

## Design patterns

### Strategy

Strategy is a behavioral design pattern. It selects an appropriate algorithm for solving a problem depending on a particular case and conditions.

Consequences of use:
- Automatic or manual algorithm selection.
- Additional layer for an algorithm choosing.
- Eliminates if conditions at client side.
- Same result is expected.
- Individual class or function need to be created for each algorithm.

### Iterator

**Iterator** is a behavioral design pattern that allows sequential access to the fields of a given object. In other words, it allows us to iterate over the elements of an object.

**Generator** is a special type of iterator that can be iterated only once. A generator does not store its results in memory.

Consequences of use:
- Results are delivered on the fly.
- Results are not stored anywhere, thus saving memory.
- We can return any number of results from all (even infinite number).
- To go through the elements, we can use a `for` loop.