# OS-HW-3: Гончаров Михаил (Б05-103)

## DB Application

### Описание

Это приложение, состоящее из двух компонентов, которые взаимодействуют друг с другом через Docker Compose.

### Шаги по запуску и использованию

#### 1. Запуск приложения с помощью Docker Compose

Запустите команду для сборки и запуска контейнеров:
```
docker-compose up -d
```

#### 2. Добавление пользователя (POST)

Для добавления пользователя (POST) запустите команду:
```
curl -X POST -H "Content-Type: application/json" -d '{"name": "Иван"}' http://localhost:3000/users
```

#### 3. Получения списка пользователей (GET)

Для получения списка пользователей (GET) запустите команду:
```
curl http://localhost:3000/users
```

Для запуска кластера:
```
minikube start
```
Для создания отдельного пода:
```
kubectl apply -f ./kubernetes/db-app-pod.yaml
```
Для создания deployment:
```
kubectl apply -f ./kubernetes/db-app-deployment.yaml 
```
Для создания сервиса:
```
kubectl expose deployment db-app --type=ClusterIP --port=3002 
```