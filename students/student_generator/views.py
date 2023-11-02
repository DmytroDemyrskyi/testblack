from django.http import HttpResponse
from faker import Faker
from .models import Student


def index(request):
    return HttpResponse("Hello world")


def student_generator(request):
    fake = Faker()
    student_data = {
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=30),
    }

    student = Student.objects.create(**student_data)

    response = f"Збережено студента: {student.first_name} {student.last_name} {student.birth_date}"
    return HttpResponse(response)


def students_generator(request):
    count = request.GET.get("count", 1)

    try:
        count = int(count)
    except ValueError:
        return HttpResponse("Помилка: 'count' повинно бути цілим числом.")

    if not 1 <= count <= 100:
        return HttpResponse("Помилка: 'count' повинно бути цілим числом від 1 до 100.")

    fake = Faker()
    saved_students = []

    for _ in range(count):
        student_data = {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=30),
        }
        student = Student.objects.create(**student_data)
        saved_students.append(student)

    student_info = "\n".join(
        [
            f"<br>{student.first_name} {student.last_name} {student.birth_date}"
            for student in saved_students
        ]
    )

    response = f"Збережено {len(saved_students)} студентів. {student_info}"
    return HttpResponse(response)
