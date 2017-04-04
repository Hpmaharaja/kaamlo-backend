Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 08:06:12) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import rethinkdb as r
>>> r.connect(host='ec2-52-33-6-252.us-west-2.compute.amazonaws.com',port=32769)
<rethinkdb.net.DefaultConnection object at 0x0000012FFD5C2C18>
>>> conn=r.connect(host='ec2-52-33-6-252.us-west-2.compute.amazonaws.com',port=32769)
>>> conn.use('mvp1')
>>> r.table('kaamloEvent')
<RqlQuery instance: r.table('kaamloEvent') >
>>> r.table('kaamloEvent').run(conn)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    r.table('kaamloEvent').run(conn)
  File "C:\Python\lib\site-packages\rethinkdb\ast.py", line 123, in run
    return c._start(self, **global_optargs)
  File "C:\Python\lib\site-packages\rethinkdb\net.py", line 625, in _start
    return self._instance.run_query(q, global_optargs.get('noreply', False))
  File "C:\Python\lib\site-packages\rethinkdb\net.py", line 471, in run_query
    raise res.make_error(query)
rethinkdb.errors.ReqlOpFailedError: Table `mvp1.kaamloEvent` does not exist in:
r.table('kaamloEvent')
^^^^^^^^^^^^^^^^^^^^^^
>>> r.table('kaamloSearch').run(conn)
<rethinkdb.net.DefaultCursor object at 0x12ffdbba550 (done streaming):
 []>
>>> r.table('kaamloSearch').insert({
    'id': 1,
    'name': 'San Francisco',
    'location': r.point(-122.423246, 37.779388)
}).run(conn)
{'deleted': 0, 'errors': 0, 'inserted': 1, 'replaced': 0, 'skipped': 0, 'unchanged': 0}
>>> r.table('kaamloSearch').run(conn)
<rethinkdb.net.DefaultCursor object at 0x12ffdbba7f0 (done streaming):
 [{'id': 1, 'location': {'$reql_type$': 'GEOMETRY', 'coordinates': [-122.423246, 37.779388], 'type': 'Point'}, 'name': 'San Francisco'}]>
>>> r.table('kaamloSearch')
<RqlQuery instance: r.table('kaamloSearch') >
>>> r.table('kaamloSearch').get(1)
<RqlQuery instance: r.table('kaamloSearch').get(1) >
>>> r.table('kaamloSearch').get(1).run(conn)
{'id': 1, 'location': {'$reql_type$': 'GEOMETRY', 'coordinates': [-122.423246, 37.779388], 'type': 'Point'}, 'name': 'San Francisco'}
>>> r.table('kaamloSearch').get(1).delete().run(conn)
{'deleted': 1, 'errors': 0, 'inserted': 0, 'replaced': 0, 'skipped': 0, 'unchanged': 0}
>>> r.table('kaamloSearch').run(conn)
<rethinkdb.net.DefaultCursor object at 0x12ffdbbaa20 (done streaming):
 []>
>>> 
