import math

def calculate_cylinder_area(radius, height):
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius**2
    total_area = lateral_area + 2 * base_area
    return total_area

def calculate_cylinder_volume(radius, height):
    volume = math.pi * radius**2 * height
    return volume
if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the cylinder: "))
        height = float(input("Enter the height of the cylinder: "))
        
        if radius <= 0 or height <= 0:
            print("Please enter positive values for radius and height.")
        else:
            area = calculate_cylinder_area(radius, height)
            volume = calculate_cylinder_volume(radius, height)
            print(f"Surface Area of the Cylinder: {area:.2f} square units")
            print(f"Volume of the Cylinder: {volume:.2f} cubic units")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for radius and height.")
