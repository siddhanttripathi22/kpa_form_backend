def standard_response(success: bool, message: str, data: any = None):
    return {
        "success": success,
        "message": message,
        "data": data,
    }
