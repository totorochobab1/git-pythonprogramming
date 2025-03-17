def get_radius(prompt):
    r=int(input(prompt))
    return r

def get_circle_area(r):
    area=r*r*3.14
    return area

n=int(input("넓이를 구하고자 하는 원의 반지름은? :"))

print("반지름", n, "인 원의 넓이 =",get_circle_area(n))
