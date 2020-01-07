from xfApp.prosanic import proflask
from xfApp.src import handler
from xfApp.src import website
from xfApp.xfMysql import createEngine
if __name__ == "__main__":
    proflask.run(host='0.0.0.0', port=49000, debug=0)
    # start()
