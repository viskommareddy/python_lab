import math
def paint_area_calculation(height,width,capacity):
    area=height*width
    number_of_cans = math.ceil(area/capacity)   #to round it to the nearest upper value

    print(f"{number_of_cans},cans are required to paint {area} units of area")
paint_area_calculation(
    height=float(input("enter the height:")),
    width=float(input("enter the width:")),
    capacity=float(input("enter the capacity of each can:"))
    )

