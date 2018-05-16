### Index the data to elasticsearch

This simple search engine can only apply to the specific strutures of the data of articles and the users.
So before we run the programme, we need make sure that the data have the following structures.</br>
Structure of user:
```javascript
{
	"id": <id>, 
	"preferences": {<category1>: <hitcounts1>, <category2>: <hitcounts2>, ...}, 
	"search_history": {<query1>: [<docid1>, <docid2>, ...], ...}
}
```
Structure of article:
```javascript
{
    "name" : <name>,
    "id" : <value>,
    "text" : <article text>,
    "categories" = [
        <cat1>, <cat2>, <cat3> ...
    ]
}
```
Run the following command to create a record of user with id of 5:
```
curl -XPOST 'http://localhost:9200/users/user/5' -H'Content-Type: application/json' -d'
{
	"id":5, 
	"preferences": {}, 
	"search_history": {}
}'
```
Run the following command to index data of articles to elasticsearch:
```
```

If you already have indices called 'articles' and 'users', you may need to delete them before with the following commands:
```
curl -XDELETE 'localhost:9200/articles'  // Delete the index of articles
```
```
curl -XDELETE 'localhost:9200/users'  // Delete the index of users
```

### Running
Make sure you start the elasticsearch server before you run the search engine.
Run the following command to launch the GUI:
```
python se_main.py
```

### Introduction to the GUI
<img src="https://github.com/gondor2222/DD2476_project/raw/LucBooost/figures/window.png" width="600"/>


