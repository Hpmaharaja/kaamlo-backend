'use strict';
// Generate a v4 UUID (random)
const uuidV4 = require('uuid/v4');

var mysql      = require('mysql');
var connection = mysql.createConnection({
  host     : 'kaamlo-db.cczywhkujcku.us-west-2.rds.amazonaws.com',
  user     : 'hpmaharaja',
  password : 'Radhe108!',
  database : 'kaamlo_db'
});

connection.connect();

exports.handler = (event, context, callback) => {

    connection.query('INSERT INTO eventInfo (eventId, eventName, startTime, endTime, goal, eventType, locationLat, locationLong, locationName) VALUES (?,?,?,?,?,?,?,?,?)',
    [ uuidV4(), event.eventName, event.startTime, event.endTime, event.goal, event.eventType, event.locationLat, event.locationLong, event.locationName ], function(err, rows, fields) {
      if (!err) {
        // console.log('The solution is: ', rows);
        console.log('Successfully inserted into eventInfo!');
        callback(null, JSON.stringify({msg: "Successfully inserted into eventInfo Table!"}));
      } else {
        console.log('Error while performing Query.');
        callback(null, JSON.stringify(err));
      }
    });

    connection.end();


};
