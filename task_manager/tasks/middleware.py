import time
import uuid
import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.perf_counter()
        request_id = str(uuid.uuid4())[:8]
        request.request_id = request_id

        response = self.get_response(request)

        duration_ms = (time.perf_counter() - start_time) * 1000
        response['X-Request-ID'] = request_id

        log_message = (
            f"[{request.method}] {request.path} | "
            f"Status: {response.status_code} | "
            f"Duration: {duration_ms:.2f}ms | "
            f"Request-ID: {request_id}"
        )

        if duration_ms > 500:
            print(f"[SLOW REQUEST] {log_message}")
        else:
            print(f"[REQUEST] {log_message}")

        return response
