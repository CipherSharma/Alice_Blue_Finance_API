In order to run the Project

Firsly go to the "Folder" containing The " manage.py " File 

Then Run the following statement in order to get the resourses needed to run the Project (You dhould already have pyhton installed in your system)
" pip install -r .\requirements.txt " (if there is an error try upgrading your pip)

After the successful installation of all the resources run the Following command 
" Python manage.py runserver "

The Django server should start running successfully.

The Project contains Three URL's Which are:
whenever you will access any of the URL's given Bilow you will have a Json Input Box where You can enter the User Details in order to access the Information provided By the API's

login/        Methode: POST     Description: Login's the user and also fetches their Session ID for the User That is used in order to access the other API's.

Input:
{
"userId":"USER_ID",
"API_KEY":"API_KEY"
}

Response:
{
    "UserID": "USER_ID",
    "EncKey": "ENC_KEY",
    "SessionID": "SESSION_ID  or AUTH_TOKEN"
}


order/        Methode: POST     Description: Places an order for the user if the user provides all the necessary information That is required in order to Place an Order.

Input:
(Test Data)
{ 
"userId":"USER_ID",
          "discqty":"0",
           "trading_symbol": "ASHOKLEY-EQ",               
           "exch":"NSE",
          "transtype":"BUY", 
          "ret":" DAY ",  
          "prctyp":"L",
          "qty":"2",
          "symbol_id": "212",
          "price":"3550.00",
          "trigPrice":"00.00",
          "pCode":"MIS",
          "complexty":"REGULAR",
          "orderTag":"order1",
"AuthToken":"AUTH_TOKEN"                 
} 

(AUTH_TOKEN is obtained from the output of the Login API it is also called "SessionID")

Response:
{
    "Response": "[{\"stat\":\"Ok\",\"NOrdNo\":\"ORDER_NO"}]"
}

orderBook/    Methode: POST     Description: This APi is used to get the Detailed data of all the orders which are Placed By the User eevn if they are rejected or completed.

Input:
{
"userId":"USER_ID",
"AuthToken":"SESSION_ID  or AUTH_TOKEN"
}

Response:
{
"Prc":"3550.00",
"RequestID":"1",
"Cancelqty":0,
"discQtyPerc":"10",
"customText":"NA",
"Mktpro":"NA",
"defmktproval":"3",
"optionType":"XX",
"usecs":"092759",
"mpro":"1",
"Qty":2,
"ordergenerationtype":"--",
"Unfilledsize":0,
"orderAuthStatus":"",
"Usercomments":"NA",
"ticksize":"5",
"Prctype":"L",
"Status":"rejected",
"Minqty":0,
"orderCriteria":"NA",
"Exseg":"nse_cm",
"Sym":"ASHOKLEY",
"multiplier":"1",
"ExchOrdID":"NA",
"ExchConfrmtime":"--",
"Pcode":"MIS",
"SyomOrderId":"",
"Dscqty":0,
"Exchange":"NSE",
"Ordvaldate":"NA",
"accountId":"679281",
"exchangeuserinfo":"111111111111100",
"Avgprc":"00.00",
"Trgprc":"00.00",
"Trantype":"B",
"bqty":"1",
"Trsym":"ASHOKLEY-EQ",
"Fillshares":0,
"AlgoCategory":"NA",
"sipindicator":"N",
"strikePrice":"00.00",
"reporttype":"failure",
"AlgoID":"NA",
"noMktPro":"0",
"BrokerClient":"--",
"OrderUserMessage":"",
"decprec":"2",
"ExpDate":"NA",
"COPercentage":0.0,
"marketprotectionpercentage":"--",
"Nstordno":"220811000223142",
"ExpSsbDate":"NA",
"OrderedTime":"11/08/2022 20:58:07",
"RejReason":"RMS: Auto Square Off Block",
"modifiedBy":"--",
"Scripname":"ASHOK LEYLAND LTD",
"stat":"Ok",
"orderentrytime":"Aug 11 2022 20:58:07",
"PriceDenomenator":"1",
"panNo":"MESPS0472L",
"RefLmtPrice":0.0,
"PriceNumerator":"1",
"token":"212",
"ordersource":"NEST_REST_WEB",
"Validity":"DAY",
"GeneralDenomenator":"1",
"series":"EQ",
"InstName":"",
"GeneralNumerator":"1",
"user":"679281",
"remarks":"order1",
"iSinceBOE":1660231687
}

(Following is the response for a Single Order)




