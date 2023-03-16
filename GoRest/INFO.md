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
 
     
