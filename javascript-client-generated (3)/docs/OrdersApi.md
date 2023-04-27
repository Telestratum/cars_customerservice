# CustomerManagementService.OrdersApi

All URIs are relative to *http://127.0.0.1:7000/customerservice/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bookingCar**](OrdersApi.md#bookingCar) | **POST** /orders | 
[**deleteOrder**](OrdersApi.md#deleteOrder) | **DELETE** /orders/{order_id} | 
[**ordersGet**](OrdersApi.md#ordersGet) | **GET** /orders | 

<a name="bookingCar"></a>
# **bookingCar**
> Model201OrderCreatedResponse bookingCar(opts)



Book a car

### Example
```javascript
import {CustomerManagementService} from 'customer_management_service';

let apiInstance = new CustomerManagementService.OrdersApi();
let opts = { 
  'body': new CustomerManagementService.OrderInfo() // OrderInfo | Booking cars
};
apiInstance.bookingCar(opts, (error, data, response) => {
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
 **body** | [**OrderInfo**](OrderInfo.md)| Booking cars | [optional] 

### Return type

[**Model201OrderCreatedResponse**](Model201OrderCreatedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

<a name="deleteOrder"></a>
# **deleteOrder**
> Model200OrderDeletedResponse deleteOrder(orderId)



delete order

### Example
```javascript
import {CustomerManagementService} from 'customer_management_service';

let apiInstance = new CustomerManagementService.OrdersApi();
let orderId = "orderId_example"; // String | 

apiInstance.deleteOrder(orderId, (error, data, response) => {
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
 **orderId** | **String**|  | 

### Return type

[**Model200OrderDeletedResponse**](Model200OrderDeletedResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

<a name="ordersGet"></a>
# **ordersGet**
> OrderDetails ordersGet()



Get  all users

### Example
```javascript
import {CustomerManagementService} from 'customer_management_service';

let apiInstance = new CustomerManagementService.OrdersApi();
apiInstance.ordersGet((error, data, response) => {
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

[**OrderDetails**](OrderDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: applications/json, application/json

