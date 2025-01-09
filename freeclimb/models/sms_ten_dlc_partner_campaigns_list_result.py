# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from freeclimb.models.sms_ten_dlc_partner_campaign import SMSTenDLCPartnerCampaign
from pydantic import StrictStr
from typing import Optional, Set
from typing_extensions import Self


class SMSTenDLCPartnerCampaignsListResult(
    BaseModel, populate_by_name=True, validate_assignment=True, protected_namespaces=()
):
    """
    SMSTenDLCPartnerCampaignsListResult
    """  # noqa: E501

    total: Optional[StrictInt] = Field(
        default=None, description="Total amount of requested resource."
    )
    start: Optional[StrictInt] = Field(
        default=None, description="Resource index at start of current page"
    )
    end: Optional[StrictInt] = Field(
        default=None, description="Resource index at end of current page"
    )
    page: Optional[StrictInt] = Field(default=None, description="Current page")
    num_pages: Optional[StrictInt] = Field(
        default=None, description="Total number of pages", alias="numPages"
    )
    page_size: Optional[StrictInt] = Field(
        default=None, description="Number of items per page", alias="pageSize"
    )
    next_page_uri: Optional[StrictStr] = Field(
        default=None,
        description="Uri to retrieve the next page of items",
        alias="nextPageUri",
    )
    partner_campaigns: Optional[List[SMSTenDLCPartnerCampaign]] = Field(
        default=None, alias="partnerCampaigns"
    )

    __properties: ClassVar[List[str]] = [
        "total",
        "start",
        "end",
        "page",
        "numPages",
        "pageSize",
        "nextPageUri",
        "partnerCampaigns",
    ]

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SMSTenDLCPartnerCampaignsListResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in partner_campaigns (list)
        _items = []
        if self.partner_campaigns:
            for _item_partner_campaigns in self.partner_campaigns:
                if _item_partner_campaigns:
                    _items.append(_item_partner_campaigns.to_dict())
            _dict["partnerCampaigns"] = _items
        # set to None if total (nullable) is None
        # and model_fields_set contains the field
        if self.total is None and "total" in self.model_fields_set:
            _dict["total"] = None

        # set to None if start (nullable) is None
        # and model_fields_set contains the field
        if self.start is None and "start" in self.model_fields_set:
            _dict["start"] = None

        # set to None if end (nullable) is None
        # and model_fields_set contains the field
        if self.end is None and "end" in self.model_fields_set:
            _dict["end"] = None

        # set to None if page (nullable) is None
        # and model_fields_set contains the field
        if self.page is None and "page" in self.model_fields_set:
            _dict["page"] = None

        # set to None if num_pages (nullable) is None
        # and model_fields_set contains the field
        if self.num_pages is None and "num_pages" in self.model_fields_set:
            _dict["numPages"] = None

        # set to None if page_size (nullable) is None
        # and model_fields_set contains the field
        if self.page_size is None and "page_size" in self.model_fields_set:
            _dict["pageSize"] = None

        # set to None if next_page_uri (nullable) is None
        # and model_fields_set contains the field
        if self.next_page_uri is None and "next_page_uri" in self.model_fields_set:
            _dict["nextPageUri"] = None

        # set to None if partner_campaigns (nullable) is None
        # and model_fields_set contains the field
        if (
            self.partner_campaigns is None
            and "partner_campaigns" in self.model_fields_set
        ):
            _dict["partnerCampaigns"] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SMSTenDLCPartnerCampaignsListResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "total": obj.get("total"),
                "start": obj.get("start"),
                "end": obj.get("end"),
                "page": obj.get("page"),
                "numPages": obj.get("numPages"),
                "pageSize": obj.get("pageSize"),
                "nextPageUri": obj.get("nextPageUri"),
                "partnerCampaigns": (
                    [
                        SMSTenDLCPartnerCampaign.from_dict(_item)
                        for _item in obj["partnerCampaigns"]
                    ]
                    if obj.get("partnerCampaigns") is not None
                    else None
                ),
            }
        )
        return _obj
