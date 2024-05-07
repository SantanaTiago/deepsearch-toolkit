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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from deepsearch.cps.apis.public_v2.models.document_artifacts_item import DocumentArtifactsItem
from deepsearch.cps.apis.public_v2.models.document_artifacts_page_item import DocumentArtifactsPageItem
from typing import Optional, Set
from typing_extensions import Self

class DocumentArtifacts(BaseModel):
    """
    DocumentArtifacts
    """ # noqa: E501
    document_meta_json: Optional[DocumentArtifactsItem] = None
    document_pdf: Optional[DocumentArtifactsItem] = None
    document_json: Optional[DocumentArtifactsItem] = None
    document_glm_json: Optional[DocumentArtifactsItem] = None
    document_md: Optional[DocumentArtifactsItem] = None
    page_pdfs: Optional[List[DocumentArtifactsPageItem]] = None
    page_images: Optional[List[DocumentArtifactsPageItem]] = None
    __properties: ClassVar[List[str]] = ["document_meta_json", "document_pdf", "document_json", "document_glm_json", "document_md", "page_pdfs", "page_images"]

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
        """Create an instance of DocumentArtifacts from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of document_meta_json
        if self.document_meta_json:
            _dict['document_meta_json'] = self.document_meta_json.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_pdf
        if self.document_pdf:
            _dict['document_pdf'] = self.document_pdf.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_json
        if self.document_json:
            _dict['document_json'] = self.document_json.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_glm_json
        if self.document_glm_json:
            _dict['document_glm_json'] = self.document_glm_json.to_dict()
        # override the default output from pydantic by calling `to_dict()` of document_md
        if self.document_md:
            _dict['document_md'] = self.document_md.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in page_pdfs (list)
        _items = []
        if self.page_pdfs:
            for _item in self.page_pdfs:
                if _item:
                    _items.append(_item.to_dict())
            _dict['page_pdfs'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in page_images (list)
        _items = []
        if self.page_images:
            for _item in self.page_images:
                if _item:
                    _items.append(_item.to_dict())
            _dict['page_images'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DocumentArtifacts from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "document_meta_json": DocumentArtifactsItem.from_dict(obj["document_meta_json"]) if obj.get("document_meta_json") is not None else None,
            "document_pdf": DocumentArtifactsItem.from_dict(obj["document_pdf"]) if obj.get("document_pdf") is not None else None,
            "document_json": DocumentArtifactsItem.from_dict(obj["document_json"]) if obj.get("document_json") is not None else None,
            "document_glm_json": DocumentArtifactsItem.from_dict(obj["document_glm_json"]) if obj.get("document_glm_json") is not None else None,
            "document_md": DocumentArtifactsItem.from_dict(obj["document_md"]) if obj.get("document_md") is not None else None,
            "page_pdfs": [DocumentArtifactsPageItem.from_dict(_item) for _item in obj["page_pdfs"]] if obj.get("page_pdfs") is not None else None,
            "page_images": [DocumentArtifactsPageItem.from_dict(_item) for _item in obj["page_images"]] if obj.get("page_images") is not None else None
        })
        return _obj


