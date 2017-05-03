'use strict';

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'kaamlo-db.cczywhkujcku.us-west-2.rds.amazonaws.com',
  user     : 'hpmaharaja',
  password : 'Radhe108!',
  database : 'kaamlo_db'
});

connection.connect();

exports.handler = (event, context, callback) => {

    connection.query('INSERT INTO attendeeInfo (eventId, userId) VALUES(?,?)',[ event.eventId, event.userId ], function(err, rows, fields) {
      if (!err) {
        // console.log('The solution is: ', rows);
        console.log('Successfully added attendeeInfo');
        callback(null, JSON.stringify({msg: "Successfully added from attendeeInfo Table!", eventId: event.eventId, userId: event.userId}));
      } else {
        console.log('Error while performing Query.');
        callback(null, JSON.stringify(err));
      }
    });

    connection.end();


};
