# Use a imagem base do Python
FROM python:3.10.12-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /src/backend

# Copia o arquivo requirements.txt para o diretório de trabalho
COPY src/backend/requirements.txt .

# Instala as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copia o conteúdo do projeto para o diretório de trabalho
COPY src/backend/ .

# Comando padrão para iniciar o servidor
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000", "--reload"]
