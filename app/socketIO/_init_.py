from flask_socketio import SocketIO

# Initialize SocketIO
socketio = SocketIO(app, cors_allowed_origins="*")

# Run app with socketio
if _name_ == '_main_':
    socketio.run(app, debug=True)