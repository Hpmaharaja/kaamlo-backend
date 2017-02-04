var express    = require("express");
var mysql      = require('mysql');
var bodyParser = require('body-parser');

var connection = mysql.createConnection({
  host     : '127.0.0.1',
  user     : 'test',
  password : 'kaamlotest',
  database : 'kaamlo'

});

connection.connect(function(err){
if(!err)
{
    console.log("Database is connected ");
} else
{
    console.log("Error connecting database ");
}
});

var app = express();
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var router=express.Router();

router.route('/events')
        .get(function(req,res){
        connection.query('SELECT eName from kaamlo.events where eName="Test"', function(err, rows, fields) {
        connection.end();
          if (!err)
            console.log('The query is: ', rows);
          else
            console.log('Error while performing Query.');
          });
          res.json({ message: 'Query Returned!' });

        })

        .post(function(req,res){
        //parameter names will be adjusted later
        var event_name=req.body.name;
        var num_people=req.body.people;
        var post={
          eName:event_name,
          people:num_people
        };
        connection.query('Insert Into kaamlo.events Set ?', post,function(err,result){
        connection.end();
          if (!err)
            console.log('Success');
          else
            console.log('Error while performing Query.');
          });
          res.json({ message: 'Query Entered' });

        });

app.use('/api',router);
app.listen(3000);
