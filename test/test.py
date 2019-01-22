from service_api.models import Student

s = Student.insert().values()
print(s)