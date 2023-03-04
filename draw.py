import json

def get_domain(scenario):
    with open("domains.json", "r") as f:
        data = json.load(f)
    return data[scenario]

def draw_classroom(canvas, students):
    num_students = len(students)
    circle_size = 70
    circle_spacing = 95
    x_pos = (1200 - circle_size * num_students - circle_spacing * (num_students-1)) / 2
    for student in students:
        y_pos = 150
        # Draw the student's circle
        canvas.create_oval(x_pos, y_pos, x_pos+circle_size, y_pos+circle_size, fill="white", outline="black", width=3)
        y_pos += circle_size + 20
        canvas.create_text(x_pos + circle_size/2, y_pos, text="Has:", font=("Arial", 15, "bold"))
        y_pos += 20
        if student["hasCalculator"]:
            canvas.create_text(x_pos + circle_size/2, y_pos, text="• Calculator", font=("Arial", 15))
            y_pos += 20
        if student["hasLaptop"]:
            canvas.create_text(x_pos + circle_size/2, y_pos, text="• Laptop", font=("Arial", 15))
            y_pos += 20
        if student["hasPencil"]:
            canvas.create_text(x_pos + circle_size/2, y_pos, text="• Pencil", font=("Arial", 15))
            y_pos += 20
        if not student["hasCalculator"] and not student["hasLaptop"] and not student["hasPencil"]:
            canvas.create_text(x_pos + circle_size/2, y_pos, text="∅", font=("Arial", 25))
        x_pos += circle_size + circle_spacing

    # Clarify domain
    canvas.create_text(600, 450, text=get_domain("classroom"), font=("Arial", 15), justify="center")

def draw_sports(canvas, people):
    # Evenly space the people with a 50px buffer
    num_people = len(people)
    circle_size = 70
    circle_spacing = 95
    x_pos = (1200 - circle_size * num_people - circle_spacing * (num_people-1)) / 2
    for person in people:
        y_pos = 100
        # Draw the person's circle
        canvas.create_oval(x_pos, y_pos, x_pos+circle_size, y_pos+circle_size, fill="white", outline="black", width=3)
        y_pos += circle_size + 20
        # Write "likes" under the person's circle
        canvas.create_text(x_pos + circle_size/2, y_pos, text="Likes:", font=("Arial", 15, "bold"))
        y_pos += 20
        if not person["likes"]:
            canvas.create_text(x_pos + circle_size/2, y_pos, text="∅", font=("Arial", 25))
            y_pos += 20
        for like in person["likes"]:
            # Draw the person's likes
            canvas.create_text(x_pos + circle_size/2, y_pos, text=f"• {like.capitalize()}", font=("Arial", 15))
            y_pos += 20
        y_pos = circle_size + 210
        canvas.create_text(x_pos + circle_size/2, y_pos, text="Dislikes:", font=("Arial", 15, "bold"))
        y_pos += 20
        if not person["dislikes"]:
            canvas.create_text(x_pos + circle_size/2, y_pos, text="∅", font=("Arial", 25))
            y_pos += 20
        for dislike in person["dislikes"]:
            # Draw the person's dislikes
            canvas.create_text(x_pos + circle_size/2, y_pos, text=f"• {dislike.capitalize()}", font=("Arial", 15))
            y_pos += 20
        x_pos += circle_size + circle_spacing

    # Clarify domain
    canvas.create_text(600, 450, text=get_domain("sports"), font=("Arial", 15), justify="center")

def draw_pets(canvas, people):
    num_people = len(people)
    circle_size = 70
    circle_spacing = 95
    x_pos = (1200 - circle_size * num_people - circle_spacing * (num_people-1)) / 2
    for person in people:
        y_pos = 100
        # Draw the person's circle
        canvas.create_oval(x_pos, y_pos, x_pos+circle_size, y_pos+circle_size, fill="white", outline="black", width=3)
        y_pos += circle_size + 20
        # Write "has" under the person's circle
        canvas.create_text(x_pos + circle_size/2, y_pos, text="Owns:", font=("Arial", 15, "bold"))
        y_pos += 20
        if not person["pets"]:
            canvas.create_text(x_pos + circle_size/2, y_pos, text="∅", font=("Arial", 25))
            y_pos += 20
        for pet in person["pets"]:
            # Draw the person's pets
            canvas.create_text(x_pos + circle_size/2, y_pos, text=f"• {pet['size'].capitalize()} {pet['type'].capitalize()}", font=("Arial", 15))
            y_pos += 20
        x_pos += circle_size + circle_spacing

    # Clarify domain
    canvas.create_text(600, 450, text=get_domain("pets"), font=("Arial", 15), justify="center")