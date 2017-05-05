'use strict';

exports.handler = (event, context, callback) => {

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'kaamlo-db.cczywhkujcku.us-west-2.rds.amazonaws.com',
  user     : 'hpmaharaja',
  password : 'Radhe108!',
  database : 'kaamlo_db'
});

connection.connect();

    connection.query('SELECT * FROM eventInfo', function(err, rows, fields) {
      if (!err) {
        // console.log('The solution is: ', rows);
        console.log('Successfully inserted into eventInfo!');
        // callback(null, JSON.stringify({msg: "Successfully inserted into eventInfo Table!", data: rows}));
        callback(null, rows);
      } else {
        console.log('Error while performing Query.');
        callback(null, JSON.stringify(err));
      }
    });

    connection.end();


};
