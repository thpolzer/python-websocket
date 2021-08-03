from kafka import KafkaConsumer
import json
import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="testuser",
    password="testuser",
    database="testuser"
    )
mycursor = mydb.cursor()

consumer = KafkaConsumer('fx-rates',value_deserializer=\
    lambda m: json.loads(m.decode('ascii')),\
        bootstrap_servers=['hadoopserver:9092'],
        auto_offset_reset='earliest', enable_auto_commit=True)

for message in consumer:
    print("topic=%s offset=%d value=%s" % (message.topic,message.offset,message.value))
    sql = "INSERT INTO fxdata (timestamp_create, eur, gbp) VALUES (%s, %s, %s)"
    val = (message.value["fx"]["timestamp"], message.value["fx"]["EUR"], message.value["fx"]["GBP"])
    mycursor.execute(sql, val)
    mydb.commit()
