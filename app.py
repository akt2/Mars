from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app=Flask(__name__)
conn = 'mongodb://localhost:27017'
mongo=pymongo.MongoClient(conn)
# db=client.mars_db
# collection=db.mars_info

# mongo=pymongo(app, uri='mongodb://localhost:27017/mars_app')

@app.route('/')
def index():
    mars_data=mongo.db.collection.find_one()
    return render_template('index.html',mars_data=mars_data)

@app.route('/scrape')
def scrape():
    mars=scrape_mars.scrape()
    mongo.db.collection.update({},mars,upsert=True)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)

