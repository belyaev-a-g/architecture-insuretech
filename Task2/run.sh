kubectl apply -f service.yaml
kubectl apply -f deployment.yaml

echo "PODS"
kubectl get pods
echo ""

echo "Services"
kubectl get service
echo ""

echo "Deployment"
kubectl get deployment
echo ""

echo "Get address on NodePort in minikube"
minikube service scaletestserv --url
echo ""


echo "HPA"
kubectl apply -f hpa.yaml
echo ""

echo "Get HPA in minikube"
kubectl get hpa
echo ""

