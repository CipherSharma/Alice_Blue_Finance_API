from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import hashlib
import requests
import json

BASE_URL="https://a3.aliceblueonline.com/rest/AliceBlueAPIService/api"
API_KEY="CqJ5EsNYuJ5eScqv3L5yHgQju3vr4e0QIHP4u9U5UkhXWbH08PkAr22zP40v38WBFGlCcUkTxBGHyHAhPOrxOmoh1yZiilYYQRfs1Vl4Cnx0AQ92DCEvjChfrdbiq9t7"

@api_view(['POST'])
def LoginAPI(request):
    URL1="/customer/getAPIEncpkey"
    URL2="/customer/getUserSID"
    Data=request.data
    userId=Data["userId"]
    url1 = BASE_URL+URL1
    url2=BASE_URL+URL2
    payload1 = json.dumps({
    "userId": userId,
    })
    headers = {
    'Content-Type': 'application/json'
    }
    response1 = requests.request("POST", url1, headers=headers, data=payload1)
    result=response1.text
    print(result)
    encKey=str(result[45:77])
    data=userId+API_KEY+encKey
    userData=hashlib.sha256(data.encode('utf8')).hexdigest()
    payload2 = json.dumps({
    "userId": userId,
    "userData":userData 
    })
    response2 = requests.request("POST", url2, headers=headers, data=payload2)
    print(response2.text)
    SessionID=response2.text[26:-2]
    return Response({"UserID":userId,"EncKey":encKey,"SessionID":SessionID }, status=status.HTTP_200_OK)

@api_view(["POST"])
def OrderAPI(request):
    URL="/placeOrder/executePlaceOrder"
    url = BASE_URL+URL
    data=request.data
    payload = json.dumps([
    {
        "discqty":data["discqty"],
        "trading_symbol":data["trading_symbol"],
        "exch":data["exch"],
        "transtype":data["transtype"], 
        "ret":data["ret"],  
        "prctyp":data["prctyp"],
        "qty":data["qty"],
        "symbol_id":data["symbol_id"],
        "price":data["price"],
        "trigPrice":data["trigPrice"],
        "pCode":data["pCode"],
        "complexty":data["complexty"],
        "orderTag":data["orderTag"]
    }
    ])
    headers = {
    'Authorization':"Bearer "+data["userId"]+" "+data["AuthToken"],
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print (response.text)
    return Response({"Response":response.text}, status=status.HTTP_200_OK)



@api_view(['POST'])
def GetOrderBookAPI(request):
    URL="/placeOrder/fetchOrderBook"
    url = BASE_URL+URL
    data=request.data
    payload={}
    headers = {
    'Authorization':"Bearer "+data["userId"]+" "+data["AuthToken"],
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)
    return Response({"Response":response.text}, status=status.HTTP_200_OK)