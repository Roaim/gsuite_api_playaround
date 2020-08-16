from ..models import ma
from ..models.hello import Hello


class HelloSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Hello


hello_schema = HelloSchema()
hello_list_schema = HelloSchema(many=True)