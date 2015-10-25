from datetime import date
import tornado.escape
import tornado.ioloop
import tornado.web
import WebSettings

gnutemp=22
class dataBuffer1(object):
    def __init__(self, temp, setpoint):
        self.temp = temp
        self.setpoint = setpoint

buffer = dataBuffer1(23,99) 
print(buffer.temp)

class VersionHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'version': '3.5.1',
                     'time_stamp':  date.today().isoformat(),
                     'temp': buffer.temp }
        self.write(response)

class SetpointHandler(tornado.web.RequestHandler):
    def get(self):
        response = { 'time_stamp':  date.today().isoformat(),
                     'setpoint': buffer.setpoint }
        self.write(response)

class UpdateSetpoint(tornado.web.RequestHandler):
    def get(self, setpoint):
        buffer.setpoint = setpoint
        response = { 'time_stamp':  date.today().isoformat(),
                     'setpoint': buffer.setpoint }
        
        self.write(response)
 
class UpdateTemperature(tornado.web.RequestHandler):
    def get(self, id):
        response = { 'temp': float(id),
                     'name': 'Crazy Game',
                     'time_stamp': date.today().isoformat() }
        buffer.temp = id
        self.write(response)
        print(buffer.temp)
        
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html", temp = buffer.temp, setpoint = buffer.setpoint)

settings = {
            "template_path": WebSettings.TEMPLATE_PATH,
            "static_path": WebSettings.STATIC_PATH,
        }

application = tornado.web.Application([
    (r"/writetemp/([-]?[\d]+[.]?[\d]+)", UpdateTemperature),
    (r"/readtemp", VersionHandler),
    (r"/setpoint/([-]?[\d]+[.]?[\d]+)", UpdateSetpoint),
    (r"/setpoint", SetpointHandler),
    (r"/main", MainHandler)
], **settings)

 
if __name__ == "__main__":
    
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()