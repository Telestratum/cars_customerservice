# CustomerManagementService.TransactionsApi

All URIs are relative to *http://127.0.0.1:7000/customerservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**addTransaction**](TransactionsApi.md#addTransaction) | **POST** /transactions | 
[**getTransactions**](TransactionsApi.md#getTransactions) | **GET** /transactions | 

<a name="addTransaction"></a>
# **addTransaction**
> TransactionDetails addTransaction(opts)



Add transaction

### Example
```javascript
import {CustomerManagementService} from 'customer_management_service';

let apiInstance = new CustomerManagementService.TransactionsApi();
let opts = { 
  'body': new CustomerManagementService.TransactionInfo() // TransactionInfo | Adding transaction
};
apiInstance.addTransaction(opts, (error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransactionInfo**](TransactionInfo.md)| Adding transaction | [optional] 

### Return type

[**TransactionDetails**](TransactionDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="getTransactions"></a>
# **getTransactions**
> TransactionDetails getTransactions()



Get transactions

### Example
```javascript
import {CustomerManagementService} from 'customer_management_service';

let apiInstance = new CustomerManagementService.TransactionsApi();
apiInstance.getTransactions((error, data, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log('API called successfully. Returned data: ' + data);
  }
});
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**TransactionDetails**](TransactionDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applications/json, application/json

