import os

from coupons.app import app


if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get("PORT", 5000))
#    if port == 5000:
#        app.debug = True
    app.run(host='0.0.0.0', port=port)
