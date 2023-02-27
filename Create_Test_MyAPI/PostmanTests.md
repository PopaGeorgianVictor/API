<strong>
    
TESTING STATUS COD

Test for the response status code:
</strong>

pm.test("Status code is 200" , () => {
    pm.response.to.have.status(200)
});
