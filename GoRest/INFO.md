## API Chain

<img src="https://i.postimg.cc/vBR24cbM/Screenshot-2023-03-16-113757.png" width="80%">


<strong>HOST:</strong>

    https://gorest.co.in

<strong>PATH:</strong> 

<i>GET:

      /public/v2/users/{id}

PUT|PATCH: 
 
     /public/v2/users/{id}
 
POST: 
    
     /public/v2/users
 
DELETE:
 
    /public/v2/users/{id}

</i>
 
## Generate random script

## <i>Create User</i>

### Pre-request Script

    var random=Math.random().toString(36).substring(2);

    var useremail = "geo"+random+"@gmail.com";
    var username = "geo"+random;

    pm.environment.set("email_env", useremail);
    pm.environment.set("name_env", username);
    
 
 
 ### Body
 
     {
     "name": "{{name_env}}",
     "gender": "male",
     "email": "{{email_env}}",
     "status": "inactive"
     }
 
 ### Tests
 
    var jsonData = JSON.parse(responseBody);
    pm.environment.set("userid_env",jsonData.id);
     
## <i>Get User Details</i>

    //validating json files in the respons
    pm.test("values of json filds", () =>
    var jsonDate=pm.response.json();
    pm.expect(jsonData.id).to.eql(pm.environment.get("userid_env"));
    pm.expect(jsonData.email).to.eql(pm.environment.g("email_env"));
    pm.expect(jsonData.name).to.eql(pm.environment.get("name_env"));
    });
    
