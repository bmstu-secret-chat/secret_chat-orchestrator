# Запуск проекта через Docker

## Предварительные требования
Для запуска проекта убедитесь, что у вас установлены:
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Запуск проекта
1. Склонируйте репозиторий и перейдите в папку проекта:
   ```bash
   git clone https://github.com/bmstu-secret-chat/secret_chat-orchestrator.git && cd secret_chat-orchestrator/
   ```
   
2. Сгенерируйте сертификаты:
   ```bash
   bash generate_certs.sh
   ``` 

3. Запустите проект с помощью Docker Compose:
   
   **a. Для Linux**:
   ```bash
   docker-compose up -d
   ```
   **b. Для Windows**:
   ```bash
   cd windows/
   ```
   ```bash
   docker-compose up -d
   ```
   Команда запускает контейнеры в фоновом режиме.

## Обновление проекта
Если вы вносите изменения в код (например, обновляете зависимости или изменяете Dockerfile), выполните команду для пересборки контейнеров:
   ```bash
   docker-compose up -d --build
   ```
Эта команда пересобирает образы и перезапускает контейнеры.

## Остановка проекта
Чтобы остановить запущенные контейнеры, выполните:
   ```bash
   docker-compose down
   ```
