### Index the data to elasticsearch

### Indexing articles
Make sure the elasticsearch engine is running.

For the 8 data files "pages_0.json", "pages_1.json", ..., "pages_7.json", use curl to post the data from the files to a bulk index http request:

```
curl -s -XPOST http://localhost:9200/_bulk -H "Content-Type: application/json" --data-binary "@PATH_TO_FILE" > out.txt
```

note that the @ is required before the filepath. The HTTP response will be stored in out.txt, in case there is an error in indexing.
Each request can take anywhere from less than a second to over ten seconds, depending on the speed of your network card and hard drive. Running on localhost with an SSD, each file takes an average of 5 seconds to index.

Once indexed, request a count of articles from your elasticsearch server by visiting "http://localhost:9200/articles/_count?"
There should be 182776 articles. You may see a slightly lower number due to locale or OS issues, in which case you will need to view the HTTP responses to find the source of the error if you wish to fix it.

### Indexing a user
```
Structure of user:
{
	"id": <id>, 
	"preferences": {<category1>: <hitcounts1>, <category2>: <hitcounts2>, ...}, 
	"search_history": {<query1>: [<docid1-1>, <docid1-2>, ...], <query2>: [<docid2-1>, <docid2-2>, ...], ...}
}
```
To index or reset your user details, run the following 

```
curl -XPOST 'http://localhost:9200/users/user/<ID>' -H 'Content-Type: application/json' -d  '<SOURCE>'
```
replace <ID> with the exact id number specified in your user source with format specified at the start of this section, and replace <SOURCE> with the full source. It may be easier to create this command as a shell script, so the entire command with the source wrapped in single quotes can be edited and executed as a file.

If all else fails, you can delete either index with:
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

MODULE REQUIREMENTS: PyQt5, numpy

Once in the GUI, you can enter a search and press "GO" to search. Searches are not submitted when you press enter; you need to click "GO".
In the "Algorithm" tab, you can switch between no reranking, category reranking, lucene boost query reranking, and the mixed algorithm. You can also toggle user updates on and off.

Normally, when the user submits a query, the search history is updated to include a query with an empty clickthrough history (unless the query exists already in the query history, in which case nothing is done). When the user clicks on an article with "update history" enabled in the algorithm tab, the user database is updated to include this new clickthrough entry every time an article is clicked. All categories associated with that article will also have their hitcounts incremented while this option is enabled.

To exactly replicate a reranking, it is often necessary to rerun the curl -XPOST command used to set the user data in the "Indexing a User" section, since clicking on articles during a session will alter behavior later in the session and in all further sessions unless the user data is reset.
