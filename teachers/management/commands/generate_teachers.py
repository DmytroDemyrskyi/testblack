from django.core.management.base import BaseCommand, CommandError
from teachers.models import Teacher

import faker

fake = faker.Faker()


class Command(BaseCommand):
    help = "Add specified number of teachers to the database"

    def add_arguments(self, parser):
        # parser.add_argument("--number", type=int, default=100)
        # в уроці ви показали перший варіант, але подобається ця команда, тому що не по іншому писати запит у консоль
        parser.add_argument("number", type=int, nargs="?", default=100)

    def handle(self, *args, **options):
        for i in range(options["number"]):
            t = Teacher.objects.create(
                name=fake.first_name(),
                surname=fake.last_name(),
                birth_date=fake.date(),
                subject=fake.job(),
            )
            self.stdout.write(
                self.style.SUCCESS('Successfully added teacher "%s"' % t.id)
            )
