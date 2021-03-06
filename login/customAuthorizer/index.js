var jwt = require('jsonwebtoken'); 
 
exports.handler =  (event, context, callback) => {
    var token = event.authorizationToken;

    jwt.verify(token, 'secret', function(err, decoded) {
        if (err) {
            callback("Unauthorized");
        } else {
            callback(null, generatePolicy('user', 'Allow', event.methodArn, decoded.userId));
        }
    });
};

var generatePolicy = function(principalId, effect, resource, userId) {
    var authResponse = {};

    authResponse.principalId = principalId;
    if (effect && resource) {
        var policyDocument = {};
        policyDocument.Version = '2012-10-17'; // default version
        policyDocument.Statement = [];
        var statementOne = {};
        statementOne.Action = 'execute-api:Invoke'; // default action
        statementOne.Effect = effect;
        statementOne.Resource = resource;
        policyDocument.Statement[0] = statementOne;
        authResponse.policyDocument = policyDocument;

        // Can optionally return a context object of your choosing.
        authResponse.context = {};
        authResponse.context.userId = userId;
    }

    return authResponse;
}
