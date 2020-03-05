##  ISO-converter server app

#### Description
Currency converter as Web API that accepts HTTP GET requests.


#### Usage
## Requirements
python version  > 3.6 ( this project uses 3.8.2)
node version v8.17.0 

The project could work on older versions as well.


## Running Tests
There are some unit tests in the tests directory.


 ```console
 foo@bar:~$ cd tests/
 foo@bar:~$ python -m unittest discover -p '*Test.py' .
 ```

## Running a basic request

First the server shold be started:

 ```console
 foo@bar:~$ cd server/
 foo@bar:~$ npm run start
 ```
then in another terminal session:
 ```console
 foo@bar:~$ ./path-to-the-project-folder/server/scripts/curl-get-example.sh
 ```
 Make sure that the scripts are executable.




