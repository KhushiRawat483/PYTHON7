t = (1, 2, 3, 2, 4, 1, 5, 1)
repeats = []

for item in t:
    if t.count(item) > 1 and item not in repeats:
        repeats.append(item)

print("Repeated items:", repeats)
