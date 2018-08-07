import rethinkdb as r 

r.connect('localhost', 28015).repl()
print(r.db_list().run())
test = r.db('test')

allDBs = r.db_list().run()
if not 'python_tutorial' in allDBs:
	r.db('python_tutorial').table_create('heroes').run()

r.db('python_tutorial').table('heroes').delete().run()

heroes = r.db('python_tutorial').table('heroes')
heroes.insert([
	{
	"hero": "batman", 
	"appearances_count": 98
	}, 
	{
	"hero": "spider-man", 
	"appearances_count": 100
	},
	{
	"hero": "iron man", 
	"appearances_count": 87
	},
]).run()

print(heroes.run())
print(heroes.filter({'hero': 'batman'}).run())
heroes.update({
	'appearances_count': r.row['appearances_count'] + 1
}).run()
print(heroes.filter(r.row['appearances_count'] >= 100).run())
print(heroes.get('d52336a9-d39b-4940-a09a-88fa82b38e1e').run())
