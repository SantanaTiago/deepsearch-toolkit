# coding: utf-8

"""
    Deep Search (DS) API

    API for Deep Search.  **WARNING**: This API is subject to change without warning!

    The version of the OpenAPI document: 3.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, SecretStr, StrictStr
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class GenAIAWSBedrockConfig(BaseModel):
    """
    Config for AWS Bedrock
    """ # noqa: E501
    genai_aws_access_key: SecretStr = Field(alias="GENAI_AWS_ACCESS_KEY")
    genai_aws_secret_key: SecretStr = Field(alias="GENAI_AWS_SECRET_KEY")
    genai_aws_region_name: StrictStr = Field(alias="GENAI_AWS_REGION_NAME")
    __properties: ClassVar[List[str]] = ["GENAI_AWS_ACCESS_KEY", "GENAI_AWS_SECRET_KEY", "GENAI_AWS_REGION_NAME"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of GenAIAWSBedrockConfig from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GenAIAWSBedrockConfig from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "GENAI_AWS_ACCESS_KEY": obj.get("GENAI_AWS_ACCESS_KEY"),
            "GENAI_AWS_SECRET_KEY": obj.get("GENAI_AWS_SECRET_KEY"),
            "GENAI_AWS_REGION_NAME": obj.get("GENAI_AWS_REGION_NAME")
        })
        return _obj


