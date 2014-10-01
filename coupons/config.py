import os

# General Flask app settings
DEBUG = os.environ.get('DEBUG', None)
SECRET_KEY = "sadasdasdas" #os.environ.get('SECRET_KEY', None)
COUPON_SAVE_DIR = "/tmp/" #os.environ.get('COUPON_SAVE_DIR', None)
QUALIFIED_MEDIA_URL = "/tmp/" #os.environ.get('QUALIFIED_MEDIA_URL', None)

# Twilio API credentials
TWILIO_ACCOUNT_SID = "ACecb5a0741d3b8570bcb094ea4dd471d4" #os.environ.get('TWILIO_ACCOUNT_SID', None)
TWILIO_AUTH_TOKEN = "61f59130f122954f9d03597adc79308e" #os.environ.get('TWILIO_AUTH_TOKEN', None)
TWILIO_NUMBER = "14048007671" #os.environ.get('TWILIO_NUMBER', None)
