from marshmallow import Schema, fields, validate

class ListItemsInput(Schema):
    items = fields.List(fields.Field(), required=True)
