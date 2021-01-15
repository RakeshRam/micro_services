# Example Django, Kubernetes and MySQL Implementation

Django App Deployed in a Kubernetes(minikube) cluster.

## <u>Deploy MySQL</u>

Component | Command
------------ | -------------
Secret | kubectl apply -f k8s\secret\mysql-srt.yaml
ConfigMap | kubectl apply -f k8s\config\mysql-cm.yaml
Volume | kubectl apply -f k8s\volumes\mysql-pv.yaml
Service | kubectl apply -f k8s\services\mysql-sv.yaml
Deployment | kubectl apply -f k8s\deployments\mysql-dp.yaml

<br/>

**Connect to MySQL:**

```bash
kubectl run -it --rm --image=mysql:5.7.22 --restart=Never mysql-client -- mysql -h db -proot
```

---

## <u>Deploy Django App</u>

Component | Command
------------ | -------------
Service | kubectl apply -f k8s\services\api-manager-sv.yaml
Deployment | kubectl apply -f k8s\deployments\api-manager-dp.yaml
Default Migrations | kubectl apply -f k8s\jobs\migration.yaml
Core App Migrations | kubectl apply -f k8s\jobs\migration-core.yaml

<br/>

**Connect to Django app instance:**

```bash
kubectl exec --stdin --tty <POD-NAME> -- /bin/sh
```
