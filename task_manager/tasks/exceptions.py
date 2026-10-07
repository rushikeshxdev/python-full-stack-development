from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        request = context.get('request')
        request_id = getattr(request, 'request_id', None)

        response.data = {
            "success": False,
            "error": {
                "code": exc.__class__.__name__,
                "details": response.data,
            },
            "request_id": request_id,
        }

    return response
