const path = require('path');
const express = require('express');
const cors = require('cors');
const mongoose = require("mongoose");
const bodyParser = require('body-parser')
const app = express();
const port = 4000;

const budgetModel = require("../models/budget_schema");
let url = 'mongodb://localhost:27017/budget_1';
mongoose.set('useCreateIndex', true);

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());
app.use(cors());
app.use('/',express.static('../public'));


app.get('/', (request, response) => {
    response.sendFile(path.join(__dirname, '../Covid-19/COVID_Fontend_files/front-end/Index.html'));
});

app.listen(port, () => {
    console.log(`API served at http://localhost:${port}`)
  });