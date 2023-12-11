from pydantic import BaseModel, ConfigDict

__all__ = [
    "ImmutableSchema",
    "MutableSchema",
]


class Schema(BaseModel):
    model_config = ConfigDict(
        use_enum_values=True,
        ser_json_bytes="utf8",
        allow_inf_nan=False,
        from_attributes=True
    )


class ImmutableSchema(Schema, frozen=True):
    ...


class MutableSchema(Schema):
    ...
