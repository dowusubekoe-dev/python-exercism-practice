def greet(name="Guest", depth=0):
    if depth > 5:  # Prevent infinite recursion by setting a depth limit
        return
    print(f"Hello, {name}!")
    greet(name="Guest", depth=depth + 1)

greet("Derek")
