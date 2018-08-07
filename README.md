# a rethinkdb tutorial 


run the rethinkdb database in another tab of your terminal and then run the code here. 

```bash 
rethinkdb
```

you can find some of the commands here:
<ul>
	<li>https://rethinkdb.com/docs/reql-data-exploration/</li>
	<li>https://rethinkdb.com/docs/sql-to-reql/python/</li>
</ul>


### notes 

1. create db

```python 
r.db('python_tutorial').table_create('heroes').run()
```

2. get all db names
 
```python 
r.db_list().run()
```

3. create table

```python 
r.db('python_tutorial').table('heroes')
```


4. insert to a table 

```python 
table_variable_name.insert([
	{}, 
	{}, 
	{}
]).run()
```


5. update values
 
```python 
heroes.update({
	'appearances_count': r.row['appearances_count'] + 1
}).run()
```


6. filter table rows based on some value 

```python 
table_variable_name.filter(r.row['appearances_count'] >= 100).run()
```


7. get a value by its id

```python 
table_variable_name.get('d7d5e949-3f71-4e21-b5b7-42b6e7048ea3').run()
```


8. delete all things that have some value 

```python 
r.table("comments").filter({"id_post": 3}).delete().run(conn)
```