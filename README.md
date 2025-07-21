# Containerized_Streamlit_app


# Build and Run the containerized app.

```bash
docker build -t openai-streamlit-app .
```

```bash
docker run -p 8501:8501 --env-file .env openai-streamlit-app
```

or using the compose file

```bash
docker-compose up --build
```