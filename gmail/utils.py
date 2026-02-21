import base64

def decode_base64(data):
    if not data:
        return None
    return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")

def extract_body(payload):
    # Case 1: direct body (no parts)
    if payload.get("body", {}).get("data"):
        return decode_base64(payload["body"]["data"])

    # Case 2: has parts (possibly nested)
    if "parts" in payload:
        for part in payload["parts"]:
            mime_type = part.get("mimeType")

            # Prefer plain text
            # if mime_type == "text/plain":
            #     data = part["body"].get("data")
            #     if data:
            #         return decode_base64(data)

            # Fallback to HTML if plain text not found
            if mime_type == "text/html":
                data = part["body"].get("data")
                if data:
                    return decode_base64(data)

            # Recursive step: check nested parts
            if "parts" in part:
                result = extract_body(part)
                if result:
                    return result

    return None
