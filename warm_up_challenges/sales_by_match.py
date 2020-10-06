pairs = 0
socks = int(input())
colors_as_string = input().split(' ')
colors = []

for x in colors_as_string:
    colors.append(int(x))

while len(colors) > 1:
    color = colors[0]
    colors.pop(0)
    try:
        color_index = colors.index(color)
        colors.pop(color_index)
        pairs += 1
    except:
        continue

print(pairs)