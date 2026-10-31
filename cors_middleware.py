def handle_cors(request, response):
    origin = request.headers.get("Origin", "")
    # Security fix: restrict CORS to trusted domain and disallow wildcard origins
    allowed_origins = ('https://app.example.com', 'https://admin.example.com')
    if origin not in allowed_origins:
        raise PermissionError("CORS policy violation: unauthorized origin")
    response.headers['Access-Control-Allow-Origin'] = origin
    return response
