#!/usr/bin/env node

var express = require('express');
var app = express();

app.listen(3000, function () {
    console.log('server running on port 3000');
})

app.get('/endpoint_name', convertIsoQuantities);

function convertIsoQuantities(req, res) {
  var spawn = require("child_process").spawn;
  var process = spawn('python', [
    "./../src/convert.py",
    req.query.arg1,
    req.query.arg2,
    req.query.arg3,
    req.query.arg4
  ]);
  process.stdout.on('data', function (data) {
    res.send(data.toString());
  });
}  
