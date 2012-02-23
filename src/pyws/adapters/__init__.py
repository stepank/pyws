from pyws.response import Response

def get_http_response_code(response):
    if response.status == Response.STATUS_ERROR:
        return '500 Internal Server Error'
    return '200 OK'

def get_http_response_code_num(response):
    return int(get_http_response_code(response).split(' ')[0])
