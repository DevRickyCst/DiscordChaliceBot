from chalice import Response


def ping_handler(event, get_response):
    if event.json_body["type"] == 1:  # PING
        return Response(status_code=200, body={"type": 1})  # PONG
    response = get_response(event)
    return response
