const express    = require('express');
const mysql      = require('mysql');
const dbconfig   = require('./config/database.js');
const connection = mysql.createConnection(dbconfig);

const app = express();

// configuration =========================
app.set('port', process.env.PORT || 3000);

app.get('/', (req, res) => {
  res.send('Root');
});

app.get('/hostings', (req, res) => {
  connection.query('SELECT * from Hosting', (error, rows) => {
    if (error) throw error;
    console.log('Hosting info is: ', rows);
    res.send(rows);
  });
});

app.get('/ipinfo', (req, res) => {
  connection.query('SELECT * from IPInfo', (error, rows) => {
    if (error) throw error;
    console.log('IPInfo info is: ', rows);
    res.send(rows);
  });
});

app.listen(app.get('port'), () => {
  console.log('Express server listening on port ' + app.get('port'));
});