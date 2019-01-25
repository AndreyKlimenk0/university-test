import json
import unittest
from service_api.app import app
from marshmallow.exceptions import ValidationError
from service_api.forms import StudentSchema


class TestStudentResources(unittest.TestCase):

    def test_post_student(self):
        data_test_student = json.dumps({
            'first_name': 'testNamePost',
            'last_name': 'testLastPost',
            'email': 'testEmail@test.com',
            'password': 'testPassword',
            'id_student_book': 1
        })
        response = app.test_client.post('/student', data=data_test_student, gather_request=False)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json['first_name'], 'testNamePost')
        self.assertEqual(response.json['last_name'], 'testLastPost')
        self.assertEqual(response.json['email'], 'testEmail@test.com')
        self.assertEqual(response.json['password'], 'testPassword')
        self.assertEqual(response.json['id_student_book'], str(1))

    def test_get__student(self):
        response = app.test_client.get('/student/31', gather_request=False)
        self.assertEqual(response.status, 200)

    def test_put_student(self):
        data = json.dumps({
            'first_name': 'testNameUpdate',
            'last_name': 'testLastName',
            'email': 'testUpdateEmail@test.com',
            'password': 'testUpdatePassword',
            'id_student_book': 2
        })
        response = app.test_client.put('/student', data=data, gather_request=False)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json['first_name'], 'testNameUpdate')
        self.assertEqual(response.json['last_name'], 'testLastName')
        self.assertEqual(response.json['email'], 'testUpdateEmail@test.com')
        self.assertEqual(response.json['password'], 'testUpdatePassword')
        self.assertEqual(response.json['id_student_book'], str(2))

    def test_delete_student(self):
        data = json.dumps({'id_student_book': 1})
        response = app.test_client.delete('/student', data=data, gather_request=False)
        self.assertEqual(response.status, 200)

    def test_student_already_exists(self):
        data_test_student = json.dumps({
            'first_name': 'testNamePost',
            'last_name': 'testLastPost',
            'email': 'testEmail@test.com',
            'password': '123456789',
            'id_student_book': 3
        })
        response = app.test_client.post('/student', data=data_test_student, gather_request=False)
        self.assertEqual(response.status, 200)

    def test_post_student_validate_email(self):
        data_test_student = json.dumps({
            'first_name': 'testNamePost',
            'last_name': 'testLastPost',
            'email': 'email@email.com',
            'password': '23462346',
            'id_student_book': 3
        })
        self.assertRaises(StudentSchema(strict=True).load(data_test_student), ValidationError)


if __name__ == '__main__':
    unittest.main()
