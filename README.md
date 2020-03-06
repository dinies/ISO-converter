# ISO-converter server app

#### Description
Currency converter as Web API that accepts HTTP GET requests.


#Usage
## Requirements and components
python version  > 3.6 ( this project uses 3.8.2)
node version v8.17.0 
npm version 6.13.4

The project could work on older versions as well.


## Running Tests
There are some unit tests in the tests directory.

 ```console
 foo@bar:~$ cd tests/
 foo@bar:~$ python -m unittest discover -p '*Test.py' .
 ```

## Running a basic request

First the server should be started:

 ```console
 foo@bar:~$ cd server/
 foo@bar:~$ npm install --save express
 foo@bar:~$ npm run start
 ```
Second, in another terminal session, run the script that executes a GET request through curl command.
But make sure that the scripts are executable.
 ```console
 foo@bar:~$ chmod +x server/scripts/curl-get-example.sh
 foo@bar:~$ ./server/scripts/curl-get-example.sh
 ```

Finally to stop the running server:
 ```console
 foo@bar:~$ cd server/
 foo@bar:~$ npm run stop
 ```





