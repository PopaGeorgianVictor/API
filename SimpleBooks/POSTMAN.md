
## Create Token

### Body

      {
      "clientName": "Postman",               => token  is generated
      "clientEmail": "geo@example.com"   
      }

## Read from CSV file

* create CSV file and populate with data

### Body 

         {
        "bookId": "{{BookID}}",
        "customerName": "{{CustomerName}}"
         }
        
        
        
### Tests

      pm.test("Status code is 201",()=>{
      pm.response.to.have.status(201);
      });

      var jsonData= JSON.parse(responseBody);
      pm.environment.set("orderid_env", jsonData.orderId);
