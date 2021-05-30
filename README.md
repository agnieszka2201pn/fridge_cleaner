#fridge_cleaner

## URI
- https://www.gmail.google.com/all/1?name=pawel&age=36
- http://127.0.0.1/elo

1. https:// - communication protocol (ftp, smtp, pop3, imap)
2. www - (pdf) - kind of resource
3. gmail - subdomain
4. google - domain
5. com - (commercial) type of website
6. all/1 - endpoint/source/path
7. ? - after ? you can pass variables
8. name=pawel - key value variable (name - klucz, pawel - value)
9. & - delimiter to pass more key value parameters


## REST API
- CRUD - create, read, update, delete (operacje które można zrobić na danych)
- User 
1. Create
    - /users (endpoint do stworzenia users. Always plural)
    - POST method
    
2. Read
    - /users (endpoint) 
    - /users/<id> (pobierze jednego użytkownika)  
    - GET method - pobierze wszystkich użytkowników
    
3. Update
    - /users/<id>
    - PUT method - update completely user
    - PATCH method - update partially user
    
4. Delete
    - /users/<id>
    - DELETE method
   
##JSON - javascript object notation
- data structure - most popular for exchanging data between apps
- XML - structured HTML
- HTML - unstructured XML
    
