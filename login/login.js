var AWS = require('aws-sdk');
var CognitoSDK = require('amazon-cognito-identity-js-node');

AWS.CognitoIdentityServiceProvider.AuthenticationDetails = CognitoSDK.AuthenticationDetails;
AWS.CognitoIdentityServiceProvider.CognitoUserPool = CognitoSDK.CognitoUserPool;
AWS.CognitoIdentityServiceProvider.CognitoUser = CognitoSDK.CognitoUser;

var UserPoolId = process.env.UserPoolId;
var ClientId = '2kiiu44inongt9mn8lm0b4l2e7';

exports.handler = (event, context, callback) => {
   authenticate(callback);
};

authenticate = (callback) => {

    var poolData = {
        UserPoolId : 'us-west-2_2pU554tQ6', // Your user pool id here
        ClientId : '2kiiu44inongt9mn8lm0b4l2e7' // Your client id here
    };

    var userPool = new AWS.CognitoIdentityServiceProvider.CognitoUserPool(poolData);

    var userData = {Username: 'madhavgharmalkar', Pool : userPool}
    var cognitoUser = new AWS.CognitoIdentityServiceProvider.CognitoUser(userData);

    var authenticationData = {Username : 'madhavgharmalkar', Password : 'KIRTANforever!5405'};
    var authenticationDetails = new AWS.CognitoIdentityServiceProvider.AuthenticationDetails(authenticationData);

    cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: function (result) {
            console.log(result);
            //callback();
        },

        mfaRequired: function(session){

        },

        newPasswordRequired: function(userAttributes, requiredAttributes) {
            cognitoUser.completeNewPasswordChallenge('KIRTANforever!5405', [],
            {
                onFailure: (err) => {
                    console.log(err);
                }
            });
        },

        onFailure: function(err) {
            console.log(err);
        },


    });
};
