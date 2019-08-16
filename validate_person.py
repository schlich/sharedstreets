def validate_fields(fields):
    fields = {k.replace(' ', ''): v for k, v in fields.items()}
    fields = {k.replace('?', ''): v for k, v in fields.items()}
