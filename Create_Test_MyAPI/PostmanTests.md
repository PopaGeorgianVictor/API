
    
## TESTING STATUS COD

### Test for the response status code:

    pm.test("Status code is 200" , () => {
    pm.response.to.have.status(200)
    }); 

### If you want to test the status code being one of a set, include them all in an array and use one of:

    pm.test("Successful GET or POST request" , () => {
    pm.expect(pm.response.code).to.be.oneOf([200,201])
    });

  
## TESTING HEADERS

### Check that a response header is prezent:
       
     pm.test("Content-Type header is present", () => {
     pm.response.to.have.header("Content-Type")
     });

### Test for a response header having a particular value: 

     pm.test("Content-Type header is application/json", () => {
     pm.expect(pm.response.headers.get("Content-Type")).to.eql('application/json; charset=utf-8')
     });

## TESTING COOKIES

### Test if a cookie is present in the response:

    pm.test("Cookie 'language' is present", () => {
    pm.expect(pm.cookies.has('language')).to.be.true;
    });

### Test for a particular cookie value:

    pm.test("Cookies language has value 1",() => {
    pm.expect(pm.cookies.get('language').to.eql('en-gb'))
    });

## TESTING RESPONSE TIME

### Test for the response time to be within a specific range:

    pm.test("Response time is less than 100ms", () => {
    pm.expect(pm.response.responseTime).to.be.below(100);
    


## ASSERTING A VALUE TYPE

### Test the type of any part of the response:

    const jsonData = pm.response.json();
    pm.test("Test data type of the response", () => {
    pm.expect(jsonData).to.be.an("object");
    pm.expect(jsonData.id).to.be.a("number");
    pm.expect(jsonData.email).to.be.a("string");
    pm.expect(jsonData.first_name).to.be.a("string");
    pm.expect(jsonData.last_name).to.be.a("string");
    pm.expect(jsonData.avatar).to.be.a("string");
    pm.expect(jsonData.courses).to.be.an("array");
    });
    
## ASSERTING ARRAY PROPERTIES

### Check if an array is empty and if it contains particular items:

    pm.test("Test array proprieties", () => {
      // courses include "Python"
    pm.expect(jsonData.courses).to.include("Python");
       // courses array must include all listed
    pm.expect(jsonData.courses).to.have.members(["Python","Selenium","MySQL"]);
    });
    
## VALIDATING JSON FILED IN RESPONSE

    pm.test("value of first_name is Georgian", () => {
    var jsonData = pm.response.json();
    pm.expect(jsonData.id).to.eql(1);
    pm.expect(jsonData.email).to.eql("popa.georgian93@gamil.com");
    pm.expect(jsonData.first_name).to.eql("Georgian");
    pm.expect(jsonData.last_name).to.eql("Popa");
    pm.expect(jsonData.avatar).to.eql("https://npg.si.edu/sites/default/files/styles/grid_wider/public/promotion/npg-npg_87_43.jpg?itok=pWuMxYem");
    pm.expect(jsonData.courses[0]).to.eql("Python");
    pm.expect(jsonData.courses[1]).to.eql("Selenium");
    pm.expect(jsonData.courses[2]).to.eql("MySQL");
    });
