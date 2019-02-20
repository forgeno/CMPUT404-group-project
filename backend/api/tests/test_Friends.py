from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework.test import RequestsClient
from ..models import Follow
import json

class AuthorProfileCase(TestCase):
    client = RequestsClient()
    username = "test123"
    password = "pw123"

    input_params = {
        "query": "friendrequest",
        "author": {
            "id": "http://127.0.0.1:5454/author/de305d54-75b4-431b-adb2-eb6b9e546013",
            "host": "http://127.0.0.1:5454/",
            "displayName": "Greg Johnson",
            "url": "http://127.0.0.1:5454/author/de305d54-75b4-431b-adb2-eb6b9e546013",
        },
        "friend": {
            "id": "http://127.0.0.1:5454/author/de305d54-75b4-431b-adb2-eb6b9e637281",
            "host": "http://127.0.0.1:5454/",
            "displayName": "Lara Croft",
            "url": "http://127.0.0.1:5454/author/de305d54-75b4-431b-adb2-eb6b9e546013",

        }
    }

    def setUp(self):
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_invalid_auth(self):
        # test if the endpoint is protected by auth
        response = self.client.post("/api/friendrequest")
        self.assertEqual(response.status_code, 403)

    def test_missing_arguments(self):
        self.client.login(username=self.username, password=self.password)
        for key in self.input_params.keys():
            invalid_input = self.input_params.copy()
            invalid_input.pop(key)
            response = self.client.post("/api/friendrequest", data=invalid_input, content_type="application/json")
            self.assertEqual(response.status_code, 400)

        for key in ["author", "friend"]:
            invalid_input = self.input_params.copy()
            invalid_input[key].pop("id")
            response = self.client.post("/api/friendrequest", data=invalid_input, content_type="application/json")
            self.assertEqual(response.status_code, 400)

    def test_invalid_methods(self):
        self.client.login(username=self.username, password=self.password)
        response = self.client.get("/api/friendrequest/")
        self.assertEqual(response.status_code, 405)
        response = self.client.put("/api/friendrequest/")
        self.assertEqual(response.status_code, 405)
        response = self.client.delete("/api/friendrequest/")
        self.assertEqual(response.status_code, 405)
        self.client.logout()

    def test_follow(self):
        Follow.objects.all().delete()
        self.client.login(username=self.username, password=self.password)

        response = self.client.post("/api/friendrequest", data=self.input_params, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), "Friend Request Success")

        row = Follow.objects.all()[0]
        self.assertEqual(row.authorA, self.input_params["author"]["id"])
        self.assertEqual(row.authorB, self.input_params["friend"]["id"])
        self.assertEqual(row.status, "FOLLOWING")

    def test_friend(self):
        Follow.objects.all().delete()
        self.client.login(username=self.username, password=self.password)

        Follow.objects.create(authorA=self.input_params["friend"]["id"],
                              authorB=self.input_params["author"]["id"],
                              status="FOLLOWING")

        response = self.client.post("/api/friendrequest", data=self.input_params, content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content), "Friend Request Success")

        results = Follow.objects.all()

        self.assertEqual(results[0].authorA, self.input_params["friend"]["id"])
        self.assertEqual(results[0].authorB, self.input_params["author"]["id"])
        self.assertEqual(results[0].status, "FRIENDS")

        self.assertEqual(results[1].authorA, self.input_params["author"]["id"])
        self.assertEqual(results[1].authorB, self.input_params["friend"]["id"])
        self.assertEqual(results[1].status, "FRIENDS")
