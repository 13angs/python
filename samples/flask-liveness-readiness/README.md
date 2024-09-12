# Flask Liveness Readiness

## How to Run the Application:

1. Run the Python script:
   ```bash
   python app.py
   ```

2. The Flask application will start and listen on port `8080`.

### Testing the Application:

1. **Check Liveness Probe**:
   - Initially, the liveness probe will always return healthy:
     ```bash
     curl http://localhost:8080/healthz
     ```
     Response:
     ```json
     {
       "status": "healthy"
     }
     ```

2. **Check Readiness Probe**:
   - Immediately after starting the app, the readiness probe will return a `503 Service Unavailable` because it takes 10 seconds to be ready:
     ```bash
     curl http://localhost:8080/ready
     ```
     Response before 10 seconds:
     ```json
     {
       "status": "not ready"
     }
     ```

   - After 10 seconds, the readiness probe will return `200 OK`:
     ```bash
     curl http://localhost:8080/ready
     ```
     Response after 10 seconds:
     ```json
     {
       "status": "ready"
     }
     ```

3. **Simulate Liveness Failure**:
   - To simulate a liveness probe failure, call:
     ```bash
     curl http://localhost:8080/fail-liveness
     ```

   - Now the liveness probe will return `500 Internal Server Error`:
     ```bash
     curl http://localhost:8080/healthz
     ```
     Response:
     ```json
     {
       "status": "unhealthy"
     }
     ```

4. **Reset Liveness Probe**:
   - To reset the liveness probe back to healthy, call:
     ```bash
     curl http://localhost:8080/reset-liveness
     ```

   - Now the liveness probe will return `200 OK` again:
     ```bash
     curl http://localhost:8080/healthz
     ```
Here’s how you can run the **Flask Liveness Readiness** application using Docker, including building the image, running it, and testing the application with Docker containers.


## Using Docker


### Run the Docker Container

You’ll need to bind the container's port to your host machine so you can access the application:

```bash
docker run -d -p 8080:8080 --name flask-app 13angs/flask-liveness-readiness:latest
```

- `-d`: Run the container in detached mode (in the background).
- `-p 8080:8080`: Bind port 8080 on the container to port 8080 on your local machine.
- `--name flask-app`: Give your container a name (optional).


### Stopping and Removing the Container

Once you are done with testing, you can stop and remove the Docker container with the following commands:

```bash
docker stop flask-app
docker rm flask-app
```

## Testing Probes in Kubernetes


### Apply the Kubernetes Configuration

1. Save the YAML file as `deployment.yaml`.
2. Deploy the app to your Kubernetes cluster:
   ```bash
   kubectl apply -f deployment.yaml
   ```

3. Check the status of the pods:
   ```bash
   kubectl get pods
   ```

4. Inspect the pod details to verify the status of the probes:
   ```bash
   kubectl describe pod <pod-name>
   ```


### Simulate Liveness Probe Failure

1. **Check the liveness probe**:
   Once the pod is running, you can simulate a liveness failure by calling the `/fail-liveness` endpoint inside the container:
   ```bash
   kubectl exec <pod-name> -- curl http://localhost:8080/fail-liveness
   ```

2. **Verify the pod restarts**:
   After simulating the failure, the liveness probe will start failing, and after 3 consecutive failures, Kubernetes will restart the pod:
   ```bash
   kubectl get pods
   ```
   The pod will have a new `RESTARTS` count.

### Simulate Readiness Probe Failure

1. **Check the readiness probe**:
   To simulate readiness failure, simply stop responding on the `/ready` endpoint (you can modify the app code to do this or simulate with other manual approaches).

2. **Verify the pod becomes unready**:
   Once the readiness probe fails, Kubernetes will stop sending traffic to this pod (it will still be running but marked as "unready"):
   ```bash
   kubectl get pods
   ```
   The `READY` column should show `0/1`, indicating the pod is not ready to receive traffic.