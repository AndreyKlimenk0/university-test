import json
import unittest
from service_api.app import app


class TestStudentResources(unittest.TestCase):

    def test_post_student(self):
        data_test_student = json.dumps({
            'first_name': 'testNamePost',
            'last_name': 'testLastPost',
            'id_student_book': 1126
        })
        response = app.test_client.post('/student', data=data_test_student, gather_request=False)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json['first_name'], 'testNamePost')
        self.assertEqual(response.json['last_name'], 'testLastPost')
        self.assertEqual(response.json['id_student_book'], str(1126))

    def test_get__student(self):
        response = app.test_client.get('/student/9', gather_request=False)
        self.assertEqual(response.status, 200)

    def test_put_student(self):
        data = json.dumps({
            'first_name': 'testNameUpdate',
            'last_name': 'testLastName',
            'id_student_book': 337
        })
        response = app.test_client.put('/student', data=data, gather_request=False)
        self.assertEqual(response.status, 200)
        self.assertEqual(response.json['first_name'], 'testNameUpdate')
        self.assertEqual(response.json['last_name'], 'testLastName')
        self.assertEqual(response.json['id_student_book'], str(337))

    def test_delete_student(self):
        data = json.dumps({'id_student_book': 395})
        response = app.test_client.delete('/student', data=data, gather_request=False)
        self.assertEqual(response.status, 200)


if __name__ == '__main__':
    unittest.main()
