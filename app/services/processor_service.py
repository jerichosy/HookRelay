from datetime import datetime


def process_webhook(payload: dict) -> dict:
    title = generate_title(payload)
    fields = extract_fields(payload)
    embed_object = {
        "title": title,
        "fields": fields,
    }
    embed_object["timestamp"] = datetime.utcnow().isoformat()

    avatar_url = get_avatar_url(payload)

    return embed_object, avatar_url

def generate_title(json_data):
    if "hookType" in json_data:
        return f"ZTNET Webhook Event: {json_data['hookType']}"
    for key in ["type", "event", "action", "name", "id"]:
        if key in json_data:
            return f"Webhook Event: {json_data[key]}"
    return "Generic Webhook Event"

def extract_fields(json_data):
    return [{"name": k, "value": str(v), "inline": True} for k, v in flatten_json(json_data).items()]

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '.')
        elif type(x) is list:
            for a, b in enumerate(x):
                flatten(b, name + str(a) + '.')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out

def get_avatar_url(json_data):
    if "hookType" in json_data:
        return "https://github.com/sinamics/ztnet/blob/main/public/ztnet_300x300.png?raw=true"
    else:
        return None
