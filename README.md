# Exercism Python Learning and Practice

## Introduction

This repository showcases my progress in mastering Python, a foundational skill for cloud automation, scripting, and infrastructure management.

### Four (4) Basic Major Features of Python

* Name Assignment (**Variables** & **Constants**)
* Functions (**def** and **return** keywords)
* Comments (gives additional information)
* Docstrings (special strings used to document a module, class, function, or method)
  * **Syntax** : They are enclosed in triple quotes (`"""` or `'''`)
  * **Placement** : The docstring should be the first statement inside a module, function, class, or method
  * **Access** : Docstrings can be accessed using the `__doc__` attribute of the object


#### Name Assignment (Variables & Constants)

**names** , also known as **Variables** can be tied to any type of object, using the <**assignment**> (**=**) operator.
* variables are always written in **snake_case**, and constants in **SCREAMING_SNAKE_CASE**.

```py
>>> my_first_program = "Python"  #<-- my_first_program bound to an string object of value Python.
>>> print(type(my_first_program))
>>> print(my_first_program)
```

```py
>>> my_car_year_module = 2019 #<-- my_car_year_module bound to an integer object of value 2019>
>>> print(type(my_car_year_module))
>>> print(my_car_year_module)
```

**Contants** are names that must be assigned once.
* defined at a module level
* visible to all **functions** and **classes**
* names must not be **re-assigned** or **value mutated**
