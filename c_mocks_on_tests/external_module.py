def external_function() -> str:
    return "original_value"

def deep_call(count=3):
    result = ""
    for _ in range(count):
        result += external_function()
    return result
