def circle(radius:float):
    area = 3.14 * radius * radius
    print(f"area of circle with radius {radius} = {area}")

def rectangle(length:float , breadth: float):
    area = length * breadth
    print(f"area of rectangle = [{area}]")

def triangle(base:float , height : float):
    area = 0.5 * height * base
    print(f"area of triangle = {area}")

if __name__ == "__main__":
    circle(56.72)