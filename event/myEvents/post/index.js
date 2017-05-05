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

    connection.query('SELECT a.* from eventInfo a WHERE a.eventId in (SELECT b.eventId FROM attendeeInfo b WHERE b.userId=?)',[event.userId], function(err, rows, fields) {
      if (!err) {
        // console.log('The solution is: ', rows);
        console.log('Successfully found events for user!');
        callback(null, rows);
      } else {
        console.log('Error while performing Query.');
        callback(null, JSON.stringify(err));
      }
    });

    connection.end();


};
