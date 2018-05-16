### Index the data to elasticsearch

This simple search engine can only apply to the specific strutures of the data of articles and the users.
So before we run the programme, we need make sure that the data have the following structures.
Structure of article:
```json
{
	"id": <id>, 
	"preferences": {"<category>": <hitcounts>, "<category>": <hitcounts>, ...}, 
	"search_history": {"<query>": ["<docid>", "<docid>", ...], ...}
}
```
Structure of user:


If you already have indices called 'articles' and 'users', you may need to delete the indices before with the following commands:
```
curl -XDELETE 'localhost:9200/articles'  // Delete the index of articles
```
```
curl -XDELETE 'localhost:9200/users'  // Delete the index of users
```

### Running

### Introduction to the GUI




