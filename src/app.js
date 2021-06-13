var express = require("express");
const cors = require('cors');
var cookieParser = require('cookie-parser')


const path= require('path')
var app = express();


// Settings 
app.set('port', process.env.PORT || 4000);

// Middlewares
app.use(cors({origin: true, credentials:true}))
app.use(express.json())
app.use(cookieParser())

// Routes

app.use('/datos', require('./routes/datos'))

module.exports = app;


