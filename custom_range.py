# 1st way to create a custom range (which i understand)
def custom_range(start, stop, step = 1):
    while start < stop:
        yield start
        start += step

for a in custom_range(1, 10, 2):
    print(a)

print("\n")

# 2nd way which i understand but 50-50
def custom_range2(start, stop, step = 1):
    current = start
    while current < stop if step > 0 else current > stop:
        yield current
        current += step

for b in custom_range2(1, 10, 2):
    print(b)

print("\n")

# 3rd way which i've just found
def custom_range3(start, stop, step = 1):
    result = []
    current = start
    while current < stop if step > 0 else current > stop:
        result.append(current)
        current += step
    return result

for c in custom_range3(1, 10, 2):
    print(c)