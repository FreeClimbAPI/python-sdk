# coding: utf-8

"""
    FreeClimb API

    FreeClimb is a cloud-based application programming interface (API) that puts the power of the Vail platform in your hands. FreeClimb simplifies the process of creating applications that can use a full range of telephony features without requiring specialized or on-site telephony equipment. Using the FreeClimb REST API to write applications is easy! You have the option to use the language of your choice or hit the API directly. Your application can execute a command by issuing a RESTful request to the FreeClimb API. The base URL to send HTTP requests to the FreeClimb REST API is: /apiserver. FreeClimb authenticates and processes your request.

    The version of the OpenAPI document: 1.0.0
    Contact: support@freeclimb.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import pydantic_core
from datetime import datetime
import freeclimb
from freeclimb import *
from freeclimb.models.tfn_campaign import TFNCampaign


class TestTFNCampaign(unittest.TestCase):
    """TFNCampaign unit test stubs"""

    def setUp(self):
        self.model = TFNCampaign(
            account_id="TS",
            campaign_id="cmptfn_387ec3f6e03b340553f35f29c8f118cdf3eae08a",
            use_case="TS",
            registration_status=SMSTollFreeCampaignRegistrationStatus.UNREGISTERED,
            date_created="TS",
            date_updated="TS",
            date_created_iso="TS",
            date_updated_iso="TS",
            revision=1,
        )

    def test_account_id(self):
        """Test TFNCampaign.account_id"""

        self.model.account_id = "TEST_STRING"
        assert self.model.account_id == "TEST_STRING"

    def test_campaign_id(self):
        """Test TFNCampaign.campaign_id"""

        self.model.campaign_id = "cmptfn_387ec3f6e03b340553f35f29c8f118cdf3eae08a"
        assert (
            self.model.campaign_id == "cmptfn_387ec3f6e03b340553f35f29c8f118cdf3eae08a"
        )

    def test_use_case(self):
        """Test TFNCampaign.use_case"""

        self.model.use_case = "TEST_STRING"
        assert self.model.use_case == "TEST_STRING"

    def test_registration_status(self):
        """Test TFNCampaign.registration_status"""
        self.model.registration_status = (
            SMSTollFreeCampaignRegistrationStatus.UNREGISTERED
        )
        assert (
            self.model.registration_status
            == SMSTollFreeCampaignRegistrationStatus.UNREGISTERED
        )
        self.model.registration_status = SMSTollFreeCampaignRegistrationStatus.INITIATED
        assert (
            self.model.registration_status
            == SMSTollFreeCampaignRegistrationStatus.INITIATED
        )
        self.model.registration_status = SMSTollFreeCampaignRegistrationStatus.PENDING
        assert (
            self.model.registration_status
            == SMSTollFreeCampaignRegistrationStatus.PENDING
        )
        self.model.registration_status = SMSTollFreeCampaignRegistrationStatus.DECLINED
        assert (
            self.model.registration_status
            == SMSTollFreeCampaignRegistrationStatus.DECLINED
        )
        self.model.registration_status = (
            SMSTollFreeCampaignRegistrationStatus.REGISTERED
        )
        assert (
            self.model.registration_status
            == SMSTollFreeCampaignRegistrationStatus.REGISTERED
        )

    def test_date_created(self):
        """Test TFNCampaign.date_created"""

        self.model.date_created = "TEST_STRING"
        assert self.model.date_created == "TEST_STRING"

    def test_date_updated(self):
        """Test TFNCampaign.date_updated"""

        self.model.date_updated = "TEST_STRING"
        assert self.model.date_updated == "TEST_STRING"

    def test_date_created_iso(self):
        """Test TFNCampaign.date_created_iso"""

        self.model.date_created_iso = "TEST_STRING"
        assert self.model.date_created_iso == "TEST_STRING"

    def test_date_updated_iso(self):
        """Test TFNCampaign.date_updated_iso"""

        self.model.date_updated_iso = "TEST_STRING"
        assert self.model.date_updated_iso == "TEST_STRING"

    def test_revision(self):
        """Test TFNCampaign.revision"""
        self.model.revision = 1
        assert self.model.revision == 1


if __name__ == "__main__":
    unittest.main()
