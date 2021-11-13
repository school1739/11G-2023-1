print("please, enter the length of the room:")
length = int(input())
print("please, enter the width of the room:")
width = int(input())
print("please, enter the height of the room")
height = int(input())
wall_area = 2 * length * height + 2 * width * height
room_area = width * length
print("wall area:" + "%f" % wall_area)
print("room area:" + "%f" % room_area)

# Evaluation: OK