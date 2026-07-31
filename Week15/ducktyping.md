# Duck Typing & Special Methods (Dunder Methods)

## Duck typing

Python doesn't care what _type_ an object is — it cares what it can _do_. "If it walks like a duck and quacks like a duck, it's a duck."

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm imitating a duck!")

def make_it_quack(thing):
    thing.quack()  # doesn't check the type, just calls the method

make_it_quack(Duck())    # Quack!
make_it_quack(Person())  # I'm imitating a duck!
```

Neither object needs to inherit from a shared base class. Python just checks: does this object have a `.quack()` method? If yes, it works.

## Special methods (dunder methods)

This is where duck typing gets powerful. Python's built-in functions and operators (`len()`, `+`, `==`, `for...in`, `print()`) don't work by magic — they work by calling special methods on your object, wrapped in double underscores ("dunder" = double underscore).

If your class defines the right dunder methods, it gets to "plug into" Python's built-in syntax and behave like a native type.

### `__repr__` and `__str__` — how objects print

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"

p = Point(1, 2)
print(p)       # Point(1, 2)  -- uses __repr__ if __str__ isn't defined
```

Without `__repr__`, printing an object gives you something unhelpful like `<__main__.Point object at 0x7f8a1c0a5d90>`.

### `__eq__` — how `==` works

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

Point(1, 2) == Point(1, 2)  # True, instead of default identity check
```

### `__len__` — how `len()` works

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

playlist = Playlist(["Song A", "Song B", "Song C"])
len(playlist)  # 3
```

### `__getitem__` — how indexing and `for` loops work

```python
class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __getitem__(self, index):
        return self.songs[index]

playlist = Playlist(["Song A", "Song B", "Song C"])
playlist[0]          # "Song A"
for song in playlist: # works automatically, no __iter__ needed!
    print(song)
```

If `__getitem__` is defined, Python can iterate over your object even without an explicit `__iter__` method — it just keeps calling `__getitem__(0)`, `__getitem__(1)`, etc. until it hits an `IndexError`.

### Other common ones

| Dunder method            | Triggered by                                         |
| ------------------------ | ---------------------------------------------------- |
| `__add__`                | `obj + other`                                        |
| `__lt__`, `__gt__`       | `obj < other`, `obj > other`                         |
| `__contains__`           | `x in obj`                                           |
| `__call__`               | `obj()` — makes an instance callable like a function |
| `__enter__` / `__exit__` | `with obj:`                                          |
| `__iter__` / `__next__`  | `for x in obj:` (the "proper" way)                   |
