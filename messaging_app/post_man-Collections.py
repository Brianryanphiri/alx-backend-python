{
	"info": {
		"_postman_id": "105bc64c-61dc-4056-a39c-222e21be5298",
		"name": "django-messaging-app",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "18648245"
	},
	"item": [
		{
			"name": "login",
			"request": {
				"auth": {
					"type": "bearer",
					"bearer": [
						{
							"key": "token",
							"value": "",
							"type": "string"
						}
					]
				},
				"method": "POST",
				"header": [],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "email",
							"value": "test@example.com",
							"type": "text"
						},
						{
							"key": "password",
							"value": "testpass123",
							"type": "text"
						},
						{
							"key": "",
							"value": "",
							"type": "text",
							"disabled": true
						}
					]
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/login/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"login",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "conversation",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMzAwMTQ4LCJpYXQiOjE3NTMyOTk4NDgsImp0aSI6IjliNTViYWU0YTUxYTQ4NGFiZGM3NDU4ZWFkOWY5NzRkIiwidXNlcl9pZCI6IjY4Yjg5NDhkLWI0MmItNDBjZC04MzFkLTZiNzA4MjRkNTFkYyJ9.OlWE31A5obDDjBESxZiQZbw9UlDWOTzvFDUO1rBf1qo",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"participants\": [\n    \"68b8948d-b42b-40cd-831d-6b70824d51dc\",\n    \"4b06e5ef-dba0-48d3-b7d8-c4e45c6a8f3a\"\n  ]\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/conversations/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"conversations",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "conversations",
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMzAwMzUwLCJpYXQiOjE3NTMzMDAwNTAsImp0aSI6IjhhYWFjYTg3NGVlMzRmYWY5ZjRmYzdjZmZhOGJmMTVhIiwidXNlcl9pZCI6IjY4Yjg5NDhkLWI0MmItNDBjZC04MzFkLTZiNzA4MjRkNTFkYyJ9.WC_JCxe0ImFkYeQVj_owRWljdgYLA1DZO6TKlrENmzg",
						"type": "text"
					}
				],
				"url": {
					"raw": "http://127.0.0.1:8000/api/conversations/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"conversations",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "message",
			"request": {
				"method": "POST",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer     eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMzAyMzYxLCJpYXQiOjE3NTMzMDIwNjEsImp0aSI6IjI3Mjg4MWI1BQZKqdp2CV3QV5nUEsqSg1ygegLmqRygjlODAxIiwidXNlcl9pZCI6IjY4Yjg5NDhkLWI0MmItNDBjZC04MzFkLTZiNzA4MjRkNTFkYyJ9.o5DlLyP9F_-uyTCoblV9IYxuNMBi_v4jKn_FErZ5TG4",
						"type": "text"
					}
				],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"message_body\": \"This is my test message\",\n  \"conversation_id\": \"cbf10304-9414-4fc8-b749-88e3e112a112\",\n  \"recipient_id\": \"68b8948d-b42b-40cd-831d-6b70824d51dc\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/messages/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"messages",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "messages",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [
					{
						"key": "Authorization",
						"value": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzUzMzAyNTYyLCJpYXQiOjE3NTMzMDIyNjIsImp0aSI6ImY1OTZmZmJmZjE4ODRjNzFhNDNhNzAwNWRkN2I2M2M5IiwidXNlcl9pZCI6IjY4Yjg5NDhkLWI0MmItNDBjZC04MzFkLTZiNzA4MjRkNTFkYyJ9.97uHqFuZrdijwx9uRmg6dp7bN17Y8clJifkT4oqLWgA",
						"type": "text"
					}
				],
				"body": {
					"mode": "formdata",
					"formdata": [
						{
							"key": "participants",
							"value": "[\"user_id_1\", \"user_id_2\"]",
							"type": "text"
						}
					]
				},
				"url": {
					"raw": "http://127.0.0.1:8000/api/messages/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"api",
						"messages",
						""
					]
				}
			},
			"response": []
		}
	]
}