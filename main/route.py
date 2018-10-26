from flask import request, jsonify
from main import app
from main.model import Table, TableSchema, table_schema, tables_schema, User, user_schema, users_schema, UserSchema, payment_schema, payments_schema, Payment, PaymentSchema, Hotel, hotel_schema, hotels_schema, HotelSchema, Menu, menu_schema, menus_schema, MenuSchema, Waiter, WaiterSchema, waiter_schema, waiters_schema, Order, OrderSchema, order_schema, orders_schema, Transaction, TransactionSchema, transaction_schema, transactions_schema, Booking, BookingSchema, booking_schema, bookings_schema, Chef, ChefSchema, chef_schema, chefs_schema
from flask_marshmallow import Marshmallow
from main import db




@app.route("/")
def func():
    return "working"

