#!/usr/bin/env node

const express = require('express')
const app = express()
const port = 3000

app.get('/', (request, response) => {
    response.send('Hello from Express!')
})

app.get('/endpoint_name', (request, response) => {
    string  = 'Hello from a complex endpoint! \n' +
      'arg1 ' + request.query.par1 + '\n' +
      'arg2 ' + request.query.par2 + '\n' +
      'arg3 ' + request.query.par3 + '\n' +
      'arg4 ' + request.query.par4 + '\n' 
    response.send( string)
})

app.get('/shoes', (request, response) => {
  order =request.query.order 
  color =request.query.color
  string =
    request.query +'\n'+
    order +'\n'+
    color +'\n'
  response.send(string)
})




app.listen(port, (err) => {
    if (err) {
          return console.log('something bad happened', err)
        }

    console.log(`server is listening on ${port}`)
})


