def handle_cors(request, response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response
