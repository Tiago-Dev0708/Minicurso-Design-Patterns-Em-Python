from flask import request as FlaskRequest
"""
def request_adapter(request: FlaskRequest):  
    return {
        "header": request.headers,
        "body": request.json,
        "query_params": dict(request.args),
        "path_params": request.view_args,
        "url": request.full_path,
        "ipv4": request.remote_addr,
    }

"""

async def request_adapter(request, user):  
    body = None
    try:
        body = request.json
    except Exception:
        body = {}
    
    headers = dict(request.headers)
    query_params = request.args
    path_params = {'user': user}


    return {
        "header": headers,
        "body": body,
        "query_params": query_params,
        "path_params": path_params,
    }
