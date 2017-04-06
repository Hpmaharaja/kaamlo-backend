import rethinkdb as r
import json

##def lambda_handler(event, context):
conn=r.connect(host='ec2-52-33-6-252.us-west-2.compute.amazonaws.com',port=32772)
conn.use('mvp1')
print(r.table('kaamloEvent').run(conn))
x={
"name":"Jeremy","location":"HB"
}





def test():
    condition = None
    for var in x:
        if(type(var)== str or type(var)==int):
            conditionForThisKey=r.row[var].eq(x[var])
        if(condition == None):
            condition=conditionForThisKey
        else:
            condition = condition.and_(conditionForThisKey)
    
    return condition
print(r.table('kaamloEvent').filter(test()).run(conn))
