//Load express module
const express = require('express');
const path = require('path');

//Put new Express app inside an app variable
const app = express();

//Set views property and view engine
app.set("views", path.resolve(__dirname, "views"));
app.set("view engine", "ejs");

const port = 8080;
//let planesArray = [] //example to pass in planes data from project

//When user hits the home page, 'hello' view shows in browser
app.get('/', (request, response) => response.render("hello", {
    //planes: planesArray
    message: "Welcome to express and EJS"
}));

//Start the express application on port 8080 and print server start message to console
app.listen(port, () => console.log('Application started listening on port 8080'));
