# SubTransactionParams

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | Amount | 
**category_id** | **int** | Category identifier. If not specified, the original transaction&#39;s category will be applied. If you explicitly want the sub-transaction to have no category, then pass this field with value &#39;0&#39; (zero). | [optional] 
**purpose** | **str** | Purpose. Maximum length is 2000. If not specified, the original transaction&#39;s value will be applied. | [optional] 
**counterpart** | **str** | Counterpart. Maximum length is 80. If not specified, the original transaction&#39;s value will be applied. | [optional] 
**counterpart_account_number** | **str** | Counterpart account number. If not specified, the original transaction&#39;s value will be applied. | [optional] 
**counterpart_iban** | **str** | Counterpart IBAN. If not specified, the original transaction&#39;s value will be applied. | [optional] 
**counterpart_bic** | **str** | Counterpart BIC. If not specified, the original transaction&#39;s value will be applied. | [optional] 
**counterpart_blz** | **str** | Counterpart BLZ. If not specified, the original transaction&#39;s value will be applied. | [optional] 
**label_ids** | **list[int]** | List of connected labels. Note that when this field is not specified, then the labels of the original transaction will NOT get applied to the sub-transaction. Instead, the sub-transaction will have no labels assigned to it. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

