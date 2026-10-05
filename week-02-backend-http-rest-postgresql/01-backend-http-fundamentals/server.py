from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse, parse_qs


# Shared tasks list
tasks = [
    {"id": 1, "title": "Learn HTTP", "done": True},
    {"id": 2, "title": "Build API", "done": False},
    {"id": 3, "title": "Learn SQL", "done": False},
    {"id": 4, "title": "Setup Postman", "done": True},
]


class MyHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        # Parse the requested URL
        parsed = urlparse(self.path)

        print(f"Incoming request path: {self.path}")

        # -----------------------------------
        # GET /tasks
        # GET /tasks?status=done
        # GET /tasks?status=pending
        # -----------------------------------
        if parsed.path == "/tasks":

            # Parse query parameters
            params = parse_qs(parsed.query)

            # Get status if it exists
            status = params.get("status", [None])[0]

            # Filter tasks
            if status == "done":
                filtered_tasks = [
                    task for task in tasks
                    if task["done"] is True
                ]

            elif status == "pending":
                filtered_tasks = [
                    task for task in tasks
                    if task["done"] is False
                ]

            else:
                filtered_tasks = tasks

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response = json.dumps(filtered_tasks)
            self.wfile.write(response.encode())

        # -----------------------------------
        # GET /tasks/<id>
        # Example: GET /tasks/2
        # -----------------------------------
        elif parsed.path.startswith("/tasks/"):

            # Split the path
            parts = parsed.path.split("/")

            # Get the ID
            task_id = int(parts[2])

            # Search for the task
            found_task = None

            for task in tasks:
                if task["id"] == task_id:
                    found_task = task
                    break

            # If task was found
            if found_task:
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                response = json.dumps(found_task)
                self.wfile.write(response.encode())

            # If task was not found
            else:
                self.send_response(404)
                self.send_header("Content-Type", "application/json")
                self.end_headers()

                response_data = {
                    "error": "Task not found"
                }

                response = json.dumps(response_data)
                self.wfile.write(response.encode())

        # -----------------------------------
        # GET /
        # -----------------------------------
        elif parsed.path == "/":

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response_data = {
                "message": "Welcome to Task Manager API!",
                "version": "1.0"
            }

            response = json.dumps(response_data)
            self.wfile.write(response.encode())

        # -----------------------------------
        # Anything else → 404
        # -----------------------------------
        else:

            self.send_response(404)
            self.send_header("Content-Type", "application/json")
            self.end_headers()

            response_data = {
                "error": "Not found"
            }

            response = json.dumps(response_data)
            self.wfile.write(response.encode())


    def do_POST(self):

        # Get the size of the request body
        content_length = int(self.headers["Content-Length"])

        # Read request body
        body = self.rfile.read(content_length)

        # JSON → Python dictionary
        data = json.loads(body.decode())

        print("Received data:", data)

        # Add new task
        tasks.append(data)

        # Send 201 Created
        self.send_response(201)

        self.send_header("Content-Type", "application/json")
        self.end_headers()

        response_data = {
            "message": "Task created",
            "task": data
        }

        response = json.dumps(response_data)

        self.wfile.write(response.encode())


# Start server
server = HTTPServer(("localhost", 8000), MyHandler)

print("Server running at http://localhost:8000")

server.serve_forever()