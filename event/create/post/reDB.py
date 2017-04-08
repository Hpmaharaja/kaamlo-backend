import rethinkdb as r
import json

def lambda_handler(event, context):
    conn=r.connect(host='ec2-52-33-6-252.us-west-2.compute.amazonaws.com',port=32772)
    conn.use('mvp1')
    print(event)
    query=r.table('kaamloEvent').insert({
        'id':r.uuid(),
        'eventName':event['eventName'],
        'start':event['start'],
        'end':event['end'],
        'goal':event['goal'],
        'type':event['type'],
        'location':event['location']
        },return_changes=True)
    newId='"'+str(query.run(conn)['changes'][0]['new_val']['id'])+'"'
    result='{"id":'+newId+"}"
    return json.loads(str(result))
