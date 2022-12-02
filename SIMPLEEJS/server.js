// load the things we need
var express = require('express');
var app = express();
const bodyParser  = require('body-parser');

// required module to make calls to a REST API
const axios = require('axios');

app.use(bodyParser.urlencoded());

// set the view engine to ejs
app.set('view engine', 'ejs');

// use res.render to load up an ejs view file

// index page 
app.get('/', function(req, res) {
    var mascots = [``
        { name: 'Sammy', organization: "DigitalOcean", birth_year: 2012},
        { name: 'Tux', organization: "Linux", birth_year: 1996},
        { name: 'Moby Dock', organization: "Docker", birth_year: 2013}
    ];
    var tagline = "No programming concept is complete without a cute animal mascot.";

    res.render('pages/index', {
        mascots: mascots,
        tagline: tagline
    });
});

// choose API page
app.get('/choose', function(req, res) {

        //itunes API call
        axios.get('https://itunes.apple.com/search?term=radiohead')
        .then((response)=>{
            let musicData = response.data;
            console.log(musicData);
            res.render('pages/choose', {
                music: musicData
            });
        });

});

// about page
app.get('/about', function(req, res) {

    //local API call to my Python REST API that delivers cars
    axios.get(`http://127.0.0.1:5000/api/car/all`)
    .then((response)=>{
        
        var cars = response.data;
        var tagline = "Here is the data coming from my own API";
        console.log(cars);
         // use res.render to load up an ejs view file
        res.render('pages/about', {
            cars: cars,
            tagline: tagline
        });
    }); 
    

    
    //get multiple service calls and combine the results in 1 function
    // axios.all([axios.get(`http://127.0.0.1:5000/api/car/all`),
    // axios.get(`http://127.0.0.1:5000/api/car?id=2`)])
    // .then(axios.spread((firstResponse, secondResponse) => {  
  
    // var cars = firstResponse.data;
    // var tagline = "Here is the data coming from my own API";
    // var aSingleCar = secondResponse.data[0];

    // //use res.render to load up an ejs view file
    // res.render('pages/about', {
    //     cars: cars,
    //     tagline: tagline,
    //     single: aSingleCar
    // });
    // }))
    // .catch(error => console.log(error)); 
    
    
});

// examples page 
app.get('/examples', function(req, res) {
    var exampleVar = "Javascript";
    
    // this will render our new example spage 
    res.render("pages/examples.ejs", {exampleVar: exampleVar});
});

app.post('/process_form', function(req, res){
    // create a variable to hold the username parsed from the request body
    var username = req.body.username
    // create a variable to hold ....
    var password = req.body.password

    let check = 0;

    if (req.body.rememberme == 'on')
            check = 1;

   console.log("email is: " + username);
   console.log("password is: " + password);
   console.log("checkedbox checked: " + check);

    res.render('pages/thanks.ejs', {body: req.body})
  
  })

  app.post('/processdynamicform', function(req, res){
    //go directly to thanks.ejs and show dynamic checkbox selection
    console.log(req.body);
    selectedID = req.body;
    for (x in req.body) {
        var selectedName = x;
        console.log("selected name is: " + selectedName);
    }
    res.render('pages/thanks.ejs', {body: req.body})
  
  })





app.listen(8080);
console.log('8080 is the magic port');
