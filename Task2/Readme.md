#  Задание 2. Динамическое масштабирование контейнеров

Выполнено горизонтальное масштабирование приложения по памяти.  
- Лимит памяти пода **30Mi**.  
- target memory utilization: `80%`;
- minReplicas: `1`;
- maxReplicas: `10`.


## Состояние деплоймента до нагрузки
Изначально запущена одна реплика сервиса.  
![hpa_before](screenshots/hpa_before.png)  

![hpa_before](screenshots/minikube_dashboard_before.png)  

![hpa_before](screenshots/minikube_dashboard_before_2.png)  

## Locust - создание нагрузки
![hpa_before](screenshots/locust_run.png)  


## Состояние деплоймента во время нагрузки
В результате нагрузки приложение масштабируется до 6 подов.  
![hpa_before](screenshots/hpa_after.png)  

![hpa_before](screenshots/minikube_dashboard_after.png)  


## Файлы задания
- `deployment.yaml` — Deployment приложения.
- `service.yaml` — Service (NodePort).
- `hpa.yaml` — HorizontalPodAutoscaler.
- `locust/locustfile.py` — сценарий нагрузки.
