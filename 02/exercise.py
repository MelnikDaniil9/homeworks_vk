import json


def parse_json(
    json_str: str, keyword_callback, required_fields=None, keywords=None
) -> None:
    if not (json_str and required_fields and keywords):
        return None
    json_doc = json.loads(json_str)
    for key in json_doc:
        if isinstance(json_doc[key], dict):
            return parse_json(
                json.dumps(json_doc.pop(key) | json_doc),
                keyword_callback,
                required_fields=required_fields,
                keywords=keywords,
            )
    for key in required_fields:
        if key in json_doc:
            for word in keywords:
                if word in json_doc[key].split():
                    keyword_callback(word)
