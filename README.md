# General
Examples of design patterns in Python.

## Design patterns

### Strategy

**Strategy** is a behavioral design pattern. It selects an appropriate algorithm for solving a problem depending on a particular case and conditions.

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

### Template method

**Template method** is a behavioral design pattern describing the general scheme of an algorithm’s operation, but requiring further specification in subclasses. It is similar to an inheritance concept with a general base class and specific derived classes.

Consequences of use:
- Creation of an abstract superclass.
- Having a method that runs all the methods of the algorithm.
- Avoidance of code duplication.

### Memento

**Memento** is a behavioral design pattern implementing the functionality of undo and redo, known from many everyday computer programs.

Consequences of use:
- Eliminates the need to create multiple instances of the same object to store its state.
- Heavily uses computer memory.
- Delegates the process of saving and loading to an external object.

In Python, there is a `pickle` library used for saving entire objects.

### Chain of responsibility

**Chain of Responsibility** is a behavioral design pattern used to pass a request sequentially among potential objects capable of processing the request until it encounters the correct one.

Consequences of use:
- Ignoring or delegating tasks further.
- Chain links can be added/removed/modified dynamically.
- The task will be performed by the first object capable of handling it.
- There may be unhandled tasks (if there is no default `handler`).
- Each element in the chain knows at most two neighboring elements.