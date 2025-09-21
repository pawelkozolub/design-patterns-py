# General
Examples of design patterns in Python.

## Design patterns

### 1. Strategy

**Strategy** is a behavioral design pattern. It selects an appropriate algorithm for solving a problem depending on a particular case and conditions.

Consequences of use:
- Automatic or manual algorithm selection.
- Additional layer for an algorithm choosing.
- Eliminates if conditions at client side.
- Same result is expected.
- Individual class or function need to be created for each algorithm.

### 2. Iterator

**Iterator** is a behavioral design pattern that allows sequential access to the fields of a given object. In other words, it allows us to iterate over the elements of an object.

**Generator** is a special type of iterator that can be iterated only once. A generator does not store its results in memory.

Consequences of use:
- Results are delivered on the fly.
- Results are not stored anywhere, thus saving memory.
- We can return any number of results from all (even infinite number).
- To go through the elements, we can use a `for` loop.

### 3. Template method

**Template method** is a behavioral design pattern describing the general scheme of an algorithm’s operation, but requiring further specification in subclasses. It is similar to an inheritance concept with a general base class and specific derived classes.

Consequences of use:
- Creation of an abstract superclass.
- Having a method that runs all the methods of the algorithm.
- Avoidance of code duplication.

### 4. Memento

**Memento** is a behavioral design pattern implementing the functionality of undo and redo, known from many everyday computer programs.

Consequences of use:
- Eliminates the need to create multiple instances of the same object to store its state.
- Heavily uses computer memory.
- Delegates the process of saving and loading to an external object.

In Python, there is a `pickle` library used for saving entire objects.

### 5. Chain of responsibility

**Chain of Responsibility** is a behavioral design pattern used to pass a request sequentially among potential objects capable of processing the request until it encounters the correct one.

Consequences of use:
- Ignoring or delegating tasks further.
- Chain links can be added/removed/modified dynamically.
- The task will be performed by the first object capable of handling it.
- There may be unhandled tasks (if there is no default `handler`).
- Each element in the chain knows at most two neighboring elements.

### 6. Command

**Command** is a behavioral design pattern that adds a layer of abstraction between a certain action and the object triggering that action.

Consequences of use:
- The command is not executed immediately. It will be executed on demand.
- The activity is separated from the object on which it is performed.
- The triggering object does not know how the final object works.
- All commands can be executed one after another or simultaneously (in parallel).

### 7. Observer

**Observer** is a behavioral design pattern that informs interested objects about the change of state of another object.

Consequences of use:
- The observer and the observed are connected only by the fact of observation – they do not need to have a similar structure.
- Removing an observer is not possible if it is on the list of the observed. In such a case, memory leaks may occur.
- Changes on both sides do not affect the observation relationship in any way.
- The list of observing objects can be changed during program operation.
- The list of observing objects can be appropriately sorted.
- The observed sends notifications to all observers.
- Observers do not know about each other.

### 8. State

**State** is a behavioral design pattern in which an object adjusts its behavior as its current state changes.

Consequences of use:
- Manual selection of the algorithm based on the device's state.
- Eliminates conditional statements.
- A separate class is created for each state.
- Adding a new state is very easy.
- States do not know about each other's existence.