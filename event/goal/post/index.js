'use strict';

var AWS = require("aws-sdk");
AWS.config.update({ region: "us-west-2" });

const tableName = "TotalEventInfo";

exports.handler = (event, context, callback) => {

    let docClient = new AWS.DynamoDB.DocumentClient();
    let params = {
        TableName: tableName,
        Item: {
            "eventId": event.eventID,
            "userId": event.userId
        }
    };

    docClient.put(params, function(err, data) {
        if (err) {
            callback(err);
        } else {
            callback(null, JSON.stringify({msg: "Successfully updated TotalEventInfo Table!"}));
        }
    });

};
