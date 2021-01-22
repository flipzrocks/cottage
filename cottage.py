from flask import Flask, render_template
from flask_socketio import SocketIO

events = [
{
  "cottage_id": "Lola's Farm",
  "cottage_description": "Lola's Farm is a great place to buy fresh local food!",
  "wares": ["Walnuts", "Pasture Chicken", "Cornbread"],
  "total_orders": 150,
  "can_deliver": False,
  "rating":3
},
{
  "cottage_id": "Kookie Karen",
  "cottage_description": "Hello I'm Karen and I make great cookies. Everyone loves the snickerdoodles!",
  "wares": ["Chocolate Chip", "Snickerdoodle", "Oatmeal Raisin"],
  "total_orders": 35,
  "can_deliver": True,
  "rating":5
}]


app = Flask(__name__)
app.config['SECRET_KEY'] = "IJustWannaDanceWithSomebody"
socketio = SocketIO(app)

@app.route("/", methods=['GET','POST'])
def root():
	return render_template('index.html', events=events)

@app.route("/test")
def sessions():
    return render_template('test.html')

def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
    socketio.run(app, debug=True)