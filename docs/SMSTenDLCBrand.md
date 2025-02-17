# SMSTenDLCBrand

A brand is a business identity behind the campaign.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the account that created this Queue. | [optional] 
**entity_type** | [**SMSTenDLCBrandEntityType**](SMSTenDLCBrandEntityType.md) |  | 
**csp_id** | **str** | Unique identifier assigned to the csp by the registry. | [optional] [readonly] 
**brand_id** | **str** | Unique identifier assigned to the brand by the registry. | [optional] [readonly] 
**first_name** | **str** | First or given name.  | [optional] 
**last_name** | **str** | Last or Surname. | [optional] 
**display_name** | **str** | Display or marketing name of the brand. | 
**company_name** | **str** | (Required for Non-profit/private/public) Legal company name. | [optional] 
**ein** | **str** | (Required for Non-profit) Government assigned corporate tax ID. EIN is 9-digits in U.S. | [optional] 
**ein_issuing_country** | **str** | ISO2 2 characters country code. Example: US - United States | [optional] 
**phone** | **str** | Valid phone number in e.164 international format. | 
**street** | **str** | Street number and name. | [optional] 
**city** | **str** | City name | [optional] 
**state** | **str** | State. Must be 2 letters code for United States. | [optional] 
**postal_code** | **str** | Postal codes. Use 5 digit zipcode for United States | [optional] 
**country** | **str** | ISO2 2 characters country code. Example: US - United States | 
**email** | **str** | Valid email address of brand support contact. | 
**stock_symbol** | **str** | (Required for public company) stock symbol. | [optional] 
**stock_exchange** | [**SMSTenDLCBrandStockExchange**](SMSTenDLCBrandStockExchange.md) |  | [optional] 
**ip_address** | **str** | IP address of the browser requesting to create brand identity. | [optional] 
**website** | **str** | Brand website URL. | [optional] 
**brand_relationship** | [**SMSTenDLCBrandRelationship**](SMSTenDLCBrandRelationship.md) |  | 
**vertical** | **str** | Vertical or industry segment of the brand. | 
**alt_business_id** | **str** | Alternate business identifier such as DUNS, LEI, or GIIN | [optional] 
**alt_business_id_type** | [**SMSTenDLCBrandAltBusinessIdType**](SMSTenDLCBrandAltBusinessIdType.md) |  | [optional] 
**universal_ein** | **str** | Universal EIN of Brand, Read Only. | [optional] [readonly] 
**reference_id** | **str** | Caller supplied brand reference ID. If supplied, the value must be unique across all submitted brands. Can be used to prevent duplicate brand registrations. | [optional] 
**optional_attributes** | **Dict[str, object]** | Optional brand attributes. Please refer to GET /enum/optionalAttributeNames for dictionary of optional attribute names. | [optional] 
**mock** | **bool** | Test brand. | 
**identity_status** | [**SMSTenDLCBrandIdentityStatus**](SMSTenDLCBrandIdentityStatus.md) |  | 
**create_date** | **datetime** | Unix timestamp when brand was created. | [optional] 

## Example

```python
from freeclimb.models.sms_ten_dlc_brand import SMSTenDLCBrand

# TODO update the JSON string below
json = "{}"
# create an instance of SMSTenDLCBrand from a JSON string
sms_ten_dlc_brand_instance = SMSTenDLCBrand.from_json(json)
# print the JSON string representation of the object
print(SMSTenDLCBrand.to_json())

# convert the object into a dict
sms_ten_dlc_brand_dict = sms_ten_dlc_brand_instance.to_dict()
# create an instance of SMSTenDLCBrand from a dict
sms_ten_dlc_brand_from_dict = SMSTenDLCBrand.from_dict(sms_ten_dlc_brand_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


