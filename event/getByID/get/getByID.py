import rethinkdb as r

        
def lambda_handler(event, context):
    conn=r.connect(host='ec2-52-33-6-252.us-west-2.compute.amazonaws.com',port=32772)
    conn.use('mvp1')
    result=(r.table('kaamloEvent').get(event['id']).run(conn))
    return (result)


    



