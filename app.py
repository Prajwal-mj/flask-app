from flask import Flask, render_template,request,redirect,url_for # For flask implementation
from bson import ObjectId # For ObjectId to work
from pymongo import MongoClient
import os

import requests
from random import randrange
