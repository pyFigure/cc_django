from jsonschema import validate
from jsonschema.exceptions import ValidationError as JsonSchemaValidationError, SchemaError
from rest_framework.exceptions import ValidationError as DrfValidationError


class JsonSchemaValidator(object):
    """
    校验 JSON 模式匹配
    只有当 required=True 时才校验
    """
    requires_context = True

    def __init__(self, schema):
        """
        @template: JSON 模板
        """
        self.schema = schema

    def __call__(self, value, serializer_field):
        try:
            validate(instance=value, schema=self.schema)
        except (JsonSchemaValidationError, SchemaError) as e:
            raise DrfValidationError(e.message)
