var express = require('express');
var app = express();


const bodyParser  = require('body-parser');
const axios = require('axios');
const { response } = require('express');

app.use(bodyParser.urlencoded());


app.set('views', __dirname + '/views')
app.set('view engine', 'ejs');

const auth = false


app.get('/', function (req, res) {
    res.render('pages/login', {})
});


app.post('/auth', function(req, res) {
    var username = req.body.username
    var password = req.body.password
    axios.get('http://127.0.0.1:5000/api/auth', {},)
        .then((response) => {
            let userData = response.data;
            console.log(userData[0].username)
            if (userData[0].username == username && userData[0].password == password) {
                res.render('pages/welcome', {
                    user: userData,
                    auth: true
                });
            } else {
                res.render('pages/login', {
                    user: 'UNAUTHORIZED',
                    auth: false
                });
            }
        });
});


app.get('/plane', function(req, res){
    axios.get('http://127.0.0.1:5000/api/plane')
        .then((response)=>{
            let planeData = response.data
            let length = planeData.length
            res.render('pages/plane', {
                plane: planeData,
                dictLength : length
            });
        });
});

app.post('/plane', function(req, res){
    var year = req.body.planeyear
    var make = req.body.planemake
    var model = req.body.planemodel
    var capacity = req.body.planecapacity
    console.log(year, capacity, make, model)
    axios.post('http://127.0.0.1:5000/api/plane', {year, make, model, capacity})
        .then((response)=>{
            res.render('pages/plane');
        });
});

app.put('/plane', function(req, res){
    var year = req.body.planeyear
    var make = req.body.planemake
    var model = req.body.planemodel
    var capacity = req.body.planecapacity
    axios.put('http://127.0.0.1:5000/api/plane', {year, make, model, capacity})
        .then((response)=>{
            let planeData = response.data
            res.render('pages/plane', {
                plane: planeData
            });
        });
});

app.delete('/plane', function(req, res){
    var year = req.body.planeyear
    var make = req.body.planemake
    var model = req.body.planemodel
    var capacity = req.body.planecapacity
    axios.delete('http://127.0.0.1:5000/api/plane', {year, make, model, capacity})
        .then((response)=>{
            res.render('pages/plane');
        });
});

app.get('/airport', function(req, res){
    axios.get('http://127.0.0.1:5000/api/airport')
        .then((response)=>{
            let airportData = response.data
            let length = airportData.length
            res.render('pages/airport', {
                airport: airportData,
                dictLength : length
            });
        });
});

app.post('/airport', function(req, res){
    var airportcode = req.body.airportcode
    var airportname = req.body.airportname
    var country = req.body.country
    axios.post('http://127.0.0.1:5000/api/airport')
        .then((response)=>{
            let airportData = response.data
            res.render('pages/airport', {
                airport: airportData
            });
        });
});

app.put('/airport', function(req, res){
    var changeairportcode = req.body.airportcode
    var changeairportname = req.body.airportname
    var changecountry = req.body.country
    var airportcode = req.body.airportcode.placeholder
    console.log(changeairportcode, changeairportname, changecountry, airportcode)
    axios.put('http://127.0.0.1:5000/api/airport')
            .then((response)=>{
            let airportData = response.data
            res.render('pages/airport', {
                airport: airportData
            });
        });
});

app.delete('/airport', function(req, res){
    var airportCode = req.body.airportcode
    var airportName = req.body.airportname
    var airportCountry = req.body.country
    axios.delete('http://127.0.0.1:5000/api/airport')
        .then((response)=>{
            let airportData = response.data
            res.render('pages/airport', {
                airport: airportData
            });
        });
});

app.get('/flight', function(req, res) {
    axios.get('http://127.0.0.1:5000/api/flight')
        .then((response)=> {
            let flightData = response.data
            let length = flightData.length
            console.log(response.data)
            console.log(length)
            res.render('pages/flight', {
                flight: flightData,
                dictLength : length
            });
        });
});


app.post('/flight', function(req, res){
    axios.post('http://127.0.0.1:5000/api/flight')
        .then((response)=> {
            let flightData = response.data
            res.render('pages/flight', {
                flight: flightData
            });
        });
});

app.delete('/flight', function(req, res){
    axios.delete('http://127.0.0.1:5000/api/flight')
        .then((response)=> {
            let flightData = response.data
            res.render('pages/flight', {
                flight: flightData
            });
        });
});

app.listen(8080);
console.log('8080 is the magic port');