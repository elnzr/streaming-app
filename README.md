# streaming-app
Pyspark Streaming example app

## How to run
1. Set `JAVA_HOME` env var
2. Run:  
`$ pip install -r requirements.txt`
3. Run in one terminal:  
`$ nc -lk 9999`
4. Run in the second terminal:  
`$ python app/streaming-app.py`
5. Paste messages in the first terminal and hit Enter:
```commandline
{"user_id": 1, "new_followers": 3}
{"user_id": 2, "new_followers": 1}
{"user_id": 2, "new_followers": 4}
{"user_id": 1, "new_followers": 3}
{"user_id": 1, "new_followers": 1}
```
6. Enjoy with the aggregated result in the second terminal:
```commandline
-------------------------------------------
Batch: 2
-------------------------------------------
+-------+------------------+
|user_id|sum(new_followers)|
+-------+------------------+
|      1|                 7|
|      2|                 5|
+-------+------------------+
```