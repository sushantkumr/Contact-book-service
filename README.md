# Contact Book service

### Run the project 
1. Clone the repository in your local machine
2. Install the requirements by running `pip3 -r install requirements.txt`
3. Initialize the database by running `python3 manage.py migrate`
4. Run the server by running `python3 manage.py runserver`
5. Run the tests by running `python3 manage.py test`


### To make use of the APIs
Open Postman while the sever is running and run the following URLs to use app.
For all requests enable Authentication --> Type as `Basic Auth` --> Username: `plivo` Password: `plivo123`

To query all contacts 
> GET: [http://127.0.0.1:8000/api/contacts/](http://127.0.0.1:8000/api/contacts/)


To insert a record
> POST: [http://127.0.0.1:8000/api/contacts/](http://127.0.0.1:8000/api/contacts/)
In Body --> Under raw format ==> 
```
{
	"name": "Post",
	"email": "terry@gmail.com",
	"mobile": 342342342
}
```
and enable `JSON(application/json)`

To modify records
> PUT: [http://127.0.0.1:8000/api/contacts/](http://127.0.0.1:8000/api/contacts/)
In Body --> Under raw format ==> Change the details similar to how it was changed under insertion of recrods
and enable `JSON(application/json)`

To delete records
> DELETE: [http://127.0.0.1:8000/api/contacts/CONTACT_ID/](http://127.0.0.1:8000/api/contacts/1/)

CONTACT_ID: Id of the contact you wish to delete
