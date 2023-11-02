from django.http import HttpResponse

from teachers.models import Teacher


# Create your views here.


def index(request):
    return HttpResponse("Nothing")


def teachers_list(request):
    teachers = Teacher.objects.all()
    teacher_info = "\n".join(
        [
            f"{teacher.id}. {teacher.name} {teacher.surname}  {teacher.birth_date}  {teacher.subject}"
            for teacher in teachers
        ]
    )
    return HttpResponse(teacher_info, content_type="text/plain")
