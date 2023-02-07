# pyutilator

pyutilator is an open source Python package that provides decorators for utility operations. Decorators are a powerful tool in Python, allowing you to modify the behavior of a function or class. pyutilator makes it easy to add common utility functions to your code, such as timing or logging, by using simple decorators.

## Installation
You can install pyutilator using pip:

``` pip install pyutilator ```

## Available Decorators

  | Decorator | Description |
  | ----------- | ----------- |
  | @print_args | Print function Arguments |
  | @print_kwargs | Print Function Key Word Arguments |
  | @print_return_value | Print Function Return Value |
 

## Usage
Here's an example of how you can use the print_args decorator to log the function arguments:

```python
from pyutilator.print.print_args import print_args

@print_args
def add(a,b):
    print("Sum : %d" %(a+b))

add(1,2)
```

```python
# output
Function Arguments : (1, 2) 
Sum : 3
```

Here's another example of how you can use the print_kwargs decorator to log the function key word arguments:
```python
from pyutilator.print.print_kwargs import print_kwargs

@print_kwargs
def add(a,b):
    print("Sum : %d" %(a+b))

add(a=1,b=2)
```

```python
# output
Function Key Word Arguments : {'a': 1, 'b': 2}
Sum : 3
```

The decorators can also be chained to perform different utility operations on the same function. This example shows how you can use both print_args and print_kwargs decorators to print function arguments and key word arguments.
```python
from pyutilator.print.print_kwargs import print_kwargs
from pyutilator.print.print_args import print_args


@print_kwargs
@print_args
def add(a,b):
    print("Sum : %d" %(a+b))

add(1,b=2)
```

```python
# output
Function Key Word Arguments : {'b': 2}
Function Arguments : (1,) 
Sum : 3
```

## Installation
You can run the :

``` pip install pyutilator ```

## Contributing
If you're interested in contributing to pyutilator, please take a look at our [contributing guidelines](https://github.com/antoprince001/pyutilator/blob/main/CONTRIBUTION.md). We welcome all contributions, whether they're bug fixes, new features, or documentation improvements.

1. Fork it (<https://github.com/antoprince001/pyutilator/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. If you've added code that should be tested, add tests.
4. Ensure the test suite passes. (`pytest`)
5. Commit your changes (`git commit -m 'Add some fooBar'`)
6. Push to the branch (`git push origin feature/fooBar`)
7. Create a new Pull Request


## License
pyutilator is released under the [MIT License](https://github.com/antoprince001/pyutilator/blob/main/LICENSE.md).



