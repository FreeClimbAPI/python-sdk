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

from freeclimb.models.sms_ten_dlc_partner_campaigns_list_result import SMSTenDLCPartnerCampaignsListResult

class TestSMSTenDLCPartnerCampaignsListResult(unittest.TestCase):
    """SMSTenDLCPartnerCampaignsListResult unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SMSTenDLCPartnerCampaignsListResult:
        """Test SMSTenDLCPartnerCampaignsListResult
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SMSTenDLCPartnerCampaignsListResult`
        """
        model = SMSTenDLCPartnerCampaignsListResult()
        if include_optional:
            return SMSTenDLCPartnerCampaignsListResult(
                total = 56,
                start = 56,
                end = 56,
                page = 56,
                num_pages = 56,
                page_size = 56,
                next_page_uri = '',
                partner_campaigns = [
                    {"campaignId":"CX56XX4","accountId":"ACe39970fb7c31c747c67148900b4d9da60a41e532","brandId":"BX56XX4","usecase":"2FA","description":"mock campaign.","sample1":"Your verification code from FreeClimb is 000000. It expires in 10 minutes.","sample2":null,"sample3":null,"sample4":null,"sample5":null,"messageFlow":null,"helpMessage":null,"status":"EXPIRED","embeddedLink":false,"embeddedPhone":false,"affiliateMarketing":false,"numberPool":false,"ageGated":false,"directLending":false,"subscriberOptin":true,"subscriberOptout":false,"subscriberHelp":true,"createDate":"2022-07-05T15:17:05Z","optinKeywords":"START","optoutKeywords":"STOP","helpKeywords":"HELP","optinMessage":"","optoutMessage":"","brand":{"optionalAttributes":{},"brandId":"BVCEBIJ","firstName":"","lastName":"","displayName":"FreeClimb LLC(mock)","companyName":"FreeClimb LLC","phone":"+18475722071","email":"bmabry@vailsys.com","website":"https://www.freeclimb.com/","evpVettingScore":22}}
                    ]
            )
        else:
            return SMSTenDLCPartnerCampaignsListResult(
        )
        """

    def testSMSTenDLCPartnerCampaignsListResult(self):
        """Test SMSTenDLCPartnerCampaignsListResult"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()