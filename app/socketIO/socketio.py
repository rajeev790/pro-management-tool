from app.socketIO import socketio

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('update_task')
def handle_update_task(data):
    socketio.emit('update_task', data, broadcast=True)