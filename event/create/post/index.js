'use strict';

var AWS = require("aws-sdk");
AWS.config.update({ region: "us-west-2" });

const uuidV4 = require('uuid/v4');
const tableName = process.env.tableName;

exports.handler = (event, context, callback) => {
    let uuid = uuidV4();

    let docClient = new AWS.DynamoDB.DocumentClient();
    let params = {
        TableName: tableName,
        Item: {
            "eventId": uuid,
            "name": event.name,
            "start": event.start,
            "end": event.end,
            "goal": event.goal,
            "location": event.location
        }
    };

    docClient.put(params, function(err, data) {
        if (err) {
            callback(err);
        } else {
            callback(null, JSON.stringify({eventId: uuid}));
        }
    });

};
