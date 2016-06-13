import flask
app = flask.Flask(__name__)

def event_stream():
    pubsub = red.pubsub()
    pubsub.subscribe('chat')
    for message in pubsub.listen():
        print message
        yield 'data: %s\n\n' % message['data']


@app.route('/post', methods=['POST'])
def post():
    message = flask.request.form['message']
    user = flask.session.get('user', 'anonymous')
    now = datetime.datetime.now().replace(microsecond=0).time()
    red.publish('chat', u'[%s] %s: %s' % (now.isoformat(), user, message))


@app.route('/stream')
def stream():
    return flask.Response(event_stream(), mimetype="text/event-stream")

@app.route('/')
def home():
    return """<script> var source = new EventSource('/stream');
source.onmessage = function (event) {
     alert(event.data);
};</script>"""

if __name__ == '__main__':
    app.debug = True
    app.run(threaded=True)
