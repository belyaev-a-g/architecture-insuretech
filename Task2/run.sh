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
