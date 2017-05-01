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

    var Query = "DELETE FROM attendeeInfo WHERE eventId=" + event.eventId + " AND userId=" + event.userId;
    console.log(Query);

    connection.query('DELETE FROM attendeeInfo WHERE eventId=? AND userId=? ',[ event.eventId, event.userId ], function(err, rows, fields) {
      if (!err) {
        // console.log('The solution is: ', rows);
        console.log('Successfully deleted attendeeInfo');
        callback(null, JSON.stringify({msg: "Successfully deleted from attendeeInfo Table!", eventId: event.eventId, userId: event.userId}));
      } else {
        console.log('Error while performing Query.');
        callback(null, JSON.stringify(err));
      }
    });

    connection.end();


};
