from flask import request, jsonify
from main import app
from main.model import Table, TableSchema, table_schema, tables_schema, User, user_schema, users_schema, UserSchema, payment_schema, payments_schema, Payment, PaymentSchema, Hotel, hotel_schema, hotels_schema, HotelSchema, Menu, menu_schema, menus_schema, MenuSchema, Waiter, WaiterSchema, waiter_schema, waiters_schema, Order, OrderSchema, order_schema, orders_schema, Transaction, TransactionSchema, transaction_schema, transactions_schema, Booking, BookingSchema, booking_schema, bookings_schema, Chef, ChefSchema, chef_schema, chefs_schema
from flask_marshmallow import Marshmallow
from main import db




@app.route("/")
def func():
    return "working"
# endpoint to create new hotels
@app.route("/hotels", methods=["POST"])
def add_hotels():
    user_id = request.form['user_id']
    hotel_name = request.form['hotel_name']
    hotel_pic = request.form['hotel_pic']
    hotel_address = request.form['hotel_address']
    hotel_email = request.form['hotel_email']
    contact = request.form['contact'] 
    hotel_lat = request.form['hotel_lat']
    hotel_long = request.form['hotel_long']
    opening_time = request.form['opening_time']
    closing_time = request.form['closing_time']
    hotel_desc = request.form['hotel_desc']
    special_monday = request.form['special_monday']
    special_tuesday = request.form['special_tuesday']
    special_wednesday = request.form['special_wednesday']
    special_thursday = request.form['special_thursday']
    special_friday = request.form['special_friday']
    special_saturday = request.form['special_saturday']
    special_sunday = request.form['special_sunday']
    bestsellers = request.form['bestsellers']
    no_waiter = request.form['no_waiter']
    no_twoseater = request.form['no_twoseater']
    no_fourseater = request.form['no_fourseater']
    no_sixseater = request.form['no_sixseater']
    no_eightseater = request.form['no_eightseater']

    new_hotel = Hotel(user_id, hotel_name, hotel_pic, hotel_address, hotel_email, contact, hotel_lat, hotel_long, opening_time, closing_time, hotel_desc, special_monday, special_tuesday, special_wednesday, special_thursday, special_friday, special_saturday, special_sunday, bestsellers, no_waiter, no_twoseater, no_fourseater, no_sixseater, no_eightseater)

    db.session.add(new_hotel)
    db.session.commit()
    return jsonify(a=new_hotel)

# endpoint to show all hotelss
@app.route("/hotels", methods=["GET"])
def get_hotels():
    all_hotels = Hotel.query.all()
    result = hotels_schema.dump(all_hotels)
    return jsonify(a=result.data)


# endpoint to get hotels detail by id
@app.route("/hotels/<hotel_id>", methods=["GET"])
def hotels_detail(hotel_id):
    hotels = Hotel.query.get(hotel_id)
    return jsonify(bestsellers=hotels.bestsellers,closing_time=hotels.closing_time,contact=hotels.contact,hotel_address=hotels.hotel_address,hotel_desc=hotels.hotel_desc, hotel_email=hotels.hotel_email,hotel_name=hotels.hotel_name,hotel_pic=hotels.hotel_pic,no_eightseater=hotels.no_eightseater, no_fourseater=hotels.no_fourseater, no_sixseater=hotels.no_sixseater, no_twoseater=hotels.no_twoseater,no_waiter=hotels.no_waiter, opening_time=hotels.opening_time, special_friday=hotels.special_friday, special_monday=hotels.special_monday, special_saturday=hotels.special_saturday, special_sunday=hotels.special_sunday, special_thursday=hotels.special_thursday, special_tuesday=hotels.special_tuesday, special_wednesday=hotels.special_wednesday,user_id= hotels.user_id)


