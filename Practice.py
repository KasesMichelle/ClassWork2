from typing import final #Immutable types  #str #int #float #bool #bytes #tuple  #Mutable types (single line comment) #list #set #dict

""" this is a multiple line comment """

number: int = 10
decimal: float = 2.5
active: bool = True

names: list = ["John", "Doe"]
name: str = 'John Doe'
marks: tuple = (1, 24, 25)  # Tuples DO allow repetition; maybe you meant they're immutable?

print(number)
print(decimal)
print(names)

def greet(name: str) -> str:
    print(name)
    return f"Welcome, {name.title()}"

print(f'Welcome, {name}')

age = 50

if age < 20:
    print('under age')
elif age > 50:
    print("senior")
else:
    print("adult")

for i in "John Doe":
    print(i)

greet("John")  # Argument = John

def add(x: int, y: int) -> int:
    return x + y

def area_circle(radius: float) -> float:
    PI: final = 3.14
    return PI * (radius ** 2)

def has_passed(average: float) -> bool:
    return average >= 50

def compute_average(scores: list[int]) -> float:
    return sum(scores) / len(scores)

def students_performance() -> None:
    name: str = input("Enter student name: ")
    print(greet(name))

    scores: list[int] = []

    for i in range(3):
        while True:
            try:
                score = int(input(f"Enter score for subject {i + 1}: "))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 & 100")
            except ValueError:
                print("Please enter a valid number")

    average_score: float = compute_average(scores)
    is_pass: bool = has_passed(average_score)

    print("\n----- Report Card -----")
    print(f"Name          : {name}")
    print(f"Scores        : {scores}")
    print(f"Average       : {average_score:.2f}")
    print(f"Status        : {'Pass' if is_pass else 'Fail'}")

    assignments_done: int = 5
    pts: float = 2.5
    total_score: float = average_score + pts

    print(f"Bonus Pts     : +{pts} for {assignments_done} assignments")
    print(f"Final Score   : {total_score:.2f}")

if __name__ == "__main__":
    students_performance()
