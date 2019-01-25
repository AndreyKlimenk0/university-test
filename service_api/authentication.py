from sanic import response

from service_api.domain.student import get_student


LOGIN_FORM = '''
<h2>Please sign in, you can try:</h2>
<dl>
<dt>Usernam</dt>
<dt>Password</dt>
</dl>
<form action="" method="POST">
  <input class="username" id="name" name="id_student_book"
    placeholder="id student book" type="text" value=""><br>
  <input class="password" id="password" name="password"
    placeholder="password" type="password" value=""><br>
  <input id="submit" name="submit" type="submit" value="Sign In">
</form>
'''

session = {}


@app.middleware('request')
async def add_session(request):
    request['session'] = session


async def login(request):

    print('req', request)
    if request.method == 'POST':
        id_student = request.form.get('id_student_book')
        password = request.form.get('password')
        print('id', id_student)
        student = await get_student(id_student)
        if id_student == student['id_student_book'] and password == student['password']:
            user = User(id=id_student, name=student['first_name'])
            auth.login_user(request, user)
            return response.redirect('/')
    return response.html(LOGIN_FORM)


async def welcome(request):
    return response.html('<h3>Welcome')

