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

    connection.query('DELETE FROM attendeeInfo WHERE eventId=? AND userId=?',[ String(event.eventId), String(event.userId) ], function(err, rows, fields) {
      if (!err) {
        // console.log('The solution is: ', rows);
        console.log('Successfully deleted attendeeInfo');
        callback(null, {msg: "Successfully deleted from attendeeInfo Table!", eventId: event.eventId, userId: event.userId});
      } else {
        console.log('Error while performing Query.');
        callback(null, JSON.stringify(err));
      }
    });

    connection.end();


};
