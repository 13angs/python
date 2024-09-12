from flask import Flask, jsonify
import time
import threading

app = Flask(__name__)

# Variables to simulate the probe behavior
is_ready = False
start_time = time.time()
liveness_status = True  # Simulates a healthy application

# Function to set readiness after a delay (simulate startup time)
def simulate_startup_delay():
    global is_ready
    time.sleep(10)  # Simulate that it takes 10 seconds for the application to be ready
    is_ready = True

# Start the readiness probe delay in a separate thread
threading.Thread(target=simulate_startup_delay).start()

# Liveness probe: Always return healthy unless manually set to unhealthy
@app.route('/healthz')
def healthz():
    if liveness_status:
        return jsonify({"status": "healthy"}), 200
    else:
        return jsonify({"status": "unhealthy"}), 500

# Readiness probe: Return healthy only after the app is ready (after 10 seconds)
@app.route('/ready')
def ready():
    if is_ready:
        return jsonify({"status": "ready"}), 200
    else:
        return jsonify({"status": "not ready"}), 503

# Endpoint to simulate failing liveness probe (for manual testing)
@app.route('/fail-liveness')
def fail_liveness():
    global liveness_status
    liveness_status = False
    return jsonify({"message": "Liveness probe set to fail"}), 200

# Endpoint to reset liveness probe to healthy
@app.route('/reset-liveness')
def reset_liveness():
    global liveness_status
    liveness_status = True
    return jsonify({"message": "Liveness probe reset to healthy"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)