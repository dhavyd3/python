#reversing using for loop
fav_colors = ['Red', 'Blue', 'Green', 'yellow', 'purple','gray']

reversed_color = fav_colors[::-1]

for color in reversed_color:
    print(color)

#Reversing using the while loop

index= len(fav_colors)

while index >=0:
    print(fav_colors[index])
    index -= 1

