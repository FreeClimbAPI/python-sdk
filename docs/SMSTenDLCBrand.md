# SMSTenDLCBrand

A brand is a business identity behind the campaign.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_type** | **str** | Entity type behind the brand. This is the form of business establishment. | 
**display_name** | **str** | Display or marketing name of the brand. | 
**phone** | **str** | Valid phone number in e.164 international format. | 
**country** | **str** | ISO2 2 characters country code. Example: US - United States | 
**email** | **str** | Valid email address of brand support contact. | 
**brand_relationship** | **str** | Brand relationship to the CSP | 
**vertical** | **str** | Vertical or industry segment of the brand. | 
**mock** | **bool** | Test brand. | 
**identity_status** | **str** | TCR assessment of the brand identification status. | 
**account_id** | **str, none_type** | ID of the account that created this Queue. | [optional] 
**csp_id** | **str** | Unique identifier assigned to the csp by the registry. | [optional] [readonly] 
**brand_id** | **str** | Unique identifier assigned to the brand by the registry. | [optional] [readonly] 
**first_name** | **str** | First or given name.  | [optional] 
**last_name** | **str** | Last or Surname. | [optional] 
**company_name** | **str** | (Required for Non-profit/private/public) Legal company name. | [optional] 
**ein** | **str** | (Required for Non-profit) Government assigned corporate tax ID. EIN is 9-digits in U.S. | [optional] 
**ein_issuing_country** | **str** | ISO2 2 characters country code. Example: US - United States | [optional] 
**street** | **str** | Street number and name. | [optional] 
**city** | **str** | City name | [optional] 
**state** | **str** | State. Must be 2 letters code for United States. | [optional] 
**postal_code** | **str** | Postal codes. Use 5 digit zipcode for United States | [optional] 
**stock_symbol** | **str** | (Required for public company) stock symbol. | [optional] 
**stock_exchange** | **str** | (Required for public company) stock exchange. | [optional] 
**ip_address** | **str** | IP address of the browser requesting to create brand identity. | [optional] 
**website** | **str** | Brand website URL. | [optional] 
**alt_business_id** | **str** | Alternate business identifier such as DUNS, LEI, or GIIN | [optional] 
**alt_business_id_type** | **str** |  | [optional] 
**universal_ein** | **str** | Universal EIN of Brand, Read Only. | [optional] [readonly] 
**reference_id** | **str** | Caller supplied brand reference ID. If supplied, the value must be unique across all submitted brands. Can be used to prevent duplicate brand registrations. | [optional] 
**optional_attributes** | **{str: ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},)}** | Optional brand attributes. Please refer to GET /enum/optionalAttributeNames for dictionary of optional attribute names. | [optional] 
**create_date** | **datetime** | Unix timestamp when brand was created. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


