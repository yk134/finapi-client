# TransactionDataWithIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_type_id** | **int** | Identifier of account type.&lt;br/&gt;&lt;br/&gt;1 &#x3D; Checking,&lt;br/&gt;2 &#x3D; Savings,&lt;br/&gt;3 &#x3D; CreditCard,&lt;br/&gt;4 &#x3D; Security,&lt;br/&gt;5 &#x3D; Loan,&lt;br/&gt;6 &#x3D; Pocket (DEPRECATED; will not be returned for any account unless this type has explicitly been set via PATCH),&lt;br/&gt;7 &#x3D; Membership,&lt;br/&gt;8 &#x3D; Bausparen&lt;br/&gt;&lt;br/&gt; | 
**amount** | **float** | Amount | 
**purpose** | **str** | Purpose. Any symbols are allowed. Maximum length is 2000. Default value: null. | [optional] 
**counterpart** | **str** | Counterpart. Any symbols are allowed. Maximum length is 80. Default value: null. | [optional] 
**counterpart_iban** | **str** | Counterpart IBAN. Default value: null. | [optional] 
**counterpart_account_number** | **str** | Counterpart account number. Default value: null. | [optional] 
**counterpart_blz** | **str** | Counterpart BLZ. Default value: null. | [optional] 
**counterpart_bic** | **str** | Counterpart BIC. Default value: null. | [optional] 
**mc_code** | **str** | Merchant category code (for credit card transactions only). Default value: null. NOTE: This field is currently not regarded. | [optional] 
**transaction_id** | **str** | Identifier of transaction. This can be any arbitrary string that will be passed back in the response so that you can map the results to the given transactions. Note that the identifier must be unique within the given list of transactions. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


