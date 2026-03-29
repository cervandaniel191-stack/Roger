from marshmallow import Schema, fields, validate

class UserSchema(Schema):
    id = fields.Int(required=True)
    username = fields.Str(required=True, validate=validate.Length(min=1))
    email = fields.Str(required=True, validate=validate.Email())
    created_at = fields.DateTime(required=True)

class OrderSchema(Schema):
    order_id = fields.Int(required=True)
    user_id = fields.Int(required=True)
    product_ids = fields.List(fields.Int(), required=True)
    total_amount = fields.Float(required=True)
    created_at = fields.DateTime(required=True)
