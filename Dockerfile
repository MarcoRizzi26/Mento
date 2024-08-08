# Use a imagem oficial do Python como base
FROM python:3.11

# Define o diretório de trabalho dentro do container
WORKDIR /src/backend/api

# Copie o arquivo requirements.txt para o diretório de trabalho
COPY src/backend/api/requirements.txt .

# Instale as dependências listadas em requirements.txt
RUN pip install upgrade pip && pip install -r requirements.txt

# Copie o restante do código da aplicação para o diretório de trabalho
COPY src/backend/api .

# Exponha a porta em que a aplicação será executada
EXPOSE 3000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
