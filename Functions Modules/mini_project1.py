def sort_colors(color_list):
    return sorted(color_list)
colors = input("Enter colors separated by commas: ").split(',')
colors = [color.strip() for color in colors]
sorted_colors = sort_colors(colors)

print("\n🎨 Sorted Colors:")
for color in sorted_colors:
    print(color)
