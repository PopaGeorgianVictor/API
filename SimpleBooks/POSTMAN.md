
## Create Token

### Body

      {
      "clientName": "Postman",               => token is generated
      "clientEmail": "geo@example.com"   
      }

## Create Order - read from CSV file

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

## Get Single Order

### Tests

      pm.test("Status code is 200", function () {
      pm.response.to.have.status(200);
      });

      pm.test("check orderid present in the response body", () => {
      var jsonData= pm.response.json();
      pm.expect(jsonData.id).to.eql(pm.environment.get("orderid_env"));
      });
      
## Delete Order + Unset variables

      pm.test("Status code is 204", function () {
      pm.response.to.have.status(204);
      });

      pm.environment.unset("orderid_env");
