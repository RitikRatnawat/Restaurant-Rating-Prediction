from flask import Flask, render_template, request
import pandas as pd
import pickle
import sklearn


app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/predictor", methods = ["GET", "POST"])
def predictor():
    columns = ['online_order', 'book_table', 'votes', 'approx_cost', 'Bakery',
                'Food Truck', 'Pub', 'Club', 'Bhojanalya', 'Delivery', 'Quick Bites', 
                'Irani Cafee', 'Takeaway', 'Dessert Parlor', 'Food Court', 'Sweet Shop', 
                'Cafe', 'Casual Dining', 'Beverage Shop', 'Microbrewery', 'Kiosk', 'Fine Dining', 
                'Lounge', 'Meat Shop', 'Bar', 'Pop Up', 'Confectionery', 'Mess', 'Dhaba', 
                'Australian', 'Tibetan', 'Cantonese', 'Mithai', 'Desserts', 'British',
                'Tea', 'Grill', 'Hot dogs', 'Gujarati', 'American', 'Afghani',
                'Mangalorean', 'Mughlai', 'Chinese', 'Mexican', 'Raw Meats',
                'Mongolian', 'Kerala', 'Pizza', 'Italian', 'Seafood', 'Sri Lankan',
                'Bihari', 'Vegan', 'Greek', 'Kebab', 'Lebanese', 'Lucknowi', 'Malwani',
                'Arabian', 'Pan Asian', 'Iranian', 'Nepalese', 'Jewish', 'Sindhi',
                'North Indian', 'Steak', 'Beverages', 'Indian', 'Spanish', 'Afghan',
                'Salad', 'Russian', 'Bar Food', 'African', 'Middle Eastern',
                'Maharashtrian', 'Ice Cream', 'Wraps', 'Thai', 'Konkan', 'Bubble Tea',
                'Fast Food', 'Assamese', 'Oriya', 'Finger Food', 'Parsi', 'French',
                'Roast Chicken', 'Korean', 'Japanese', 'Tex-Mex', 'Naga', 'Rajasthani',
                'Biryani', 'Charcoal Chicken', 'Sushi', 'Juices', 'Singaporean', 'Drinks Only', 
                'Momos', 'Vietnamese', 'BBQ', 'Coffee', 'Kashmiri','European', 'Modern Indian', 
                'Mediterranean', 'Healthy Food', 'Andhra', 'North Eastern', 'German', 'Chettinad', 
                'Continental', 'Bengali', 'Hyderabadi', 'Indonesian', 'Malaysian', 'Paan', 'Burger', 
                'Sandwich', 'Bohri', 'South Indian', 'Goan', 'Tamil', 'Portuguese', 'South American', 
                'Awadhi', 'Belgian', 'Street Food', 'Turkish', 'Rolls', 'Asian', 'Burmese', 'BTM', 
                'Banashankari', 'Banaswadi', 'Bannerghatta Road', 'Basavanagudi', 'Basaveshwara Nagar', 
                'Bellandur', 'Bommanahalli', 'Brigade Road', 'Brookefield', 'CV Raman Nagar',
                'Central Bangalore', 'Church Street', 'City Market', 'Commercial Street', 'Cunningham Road', 
                'Domlur', 'East Bangalore', 'Ejipura', 'Electronic City', 'Frazer Town', 'HBR Layout', 'HSR', 
                'Hebbal', 'Hennur', 'Hosur Road', 'ITPL Main Road, Whitefield', 'Indiranagar','Infantry Road', 
                'JP Nagar', 'Jakkur', 'Jalahalli', 'Jayanagar', 'Jeevan Bhima Nagar', 'KR Puram', 'Kaggadasapura', 
                'Kalyan Nagar', 'Kammanahalli', 'Kanakapura Road', 'Kengeri', 'Koramangala','Koramangala 1st Block',
                'Koramangala 2nd Block','Koramangala 3rd Block', 'Koramangala 4th Block', 'Koramangala 5th Block', 
                'Koramangala 6th Block', 'Koramangala 7th Block', 'Koramangala 8th Block', 'Kumaraswamy Layout',
                'Langford Town', 'Lavelle Road', 'MG Road', 'Magadi Road', 'Majestic', 'Malleshwaram', 'Marathahalli', 
                'Mysore Road', 'Nagarbhavi', 'Nagawara', 'New BEL Road', 'North Bangalore', 'Old Airport Road',
                'Old Madras Road', 'Peenya', 'RT Nagar', 'Race Course Road', 'Rajajinagar', 'Rajarajeshwari Nagar',
                'Rammurthy Nagar', 'Residency Road', 'Richmond Road', 'Sadashiv Nagar', 'Sahakara Nagar', 'Sanjay Nagar', 
                'Sankey Road', 'Sarjapur Road', 'Seshadripuram', 'Shanti Nagar', 'Shivajinagar', 'South Bangalore',
                'St. Marks Road', 'Thippasandra', 'Ulsoor', 'Uttarahalli', 'Varthur Main Road, Whitefield', 'Vasanth Nagar', 
                'Vijay Nagar', 'West Bangalore', 'Whitefield', 'Wilson Garden', 'Yelahanka', 'Yeshwantpur']
     
    return render_template("predictor.html")

@app.route("/aboutUs")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug = True)