from flask import Flask, render_template, redirect
import pymongo
import mars2

app=Flask(__name__)
mongo = pymongo(app, url='mongodb://localhost:27017/mars_app')

@app.route('/')
def home():
    mars_data=mongo.db.collection.find_one()
    return render_template('index.html',ares=mars_data)

@app.route('/scrape')
def scrape():
    ares_data=scrape_mars.scrape()
    mongo.db.collection.update({},ares_data, upsert=True)
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)
