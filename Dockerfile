# Usar uma imagem base oficial do Python
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de requisitos
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o conteúdo do diretório atual para o diretório de trabalho no contêiner
COPY . .

# Comando para rodar a aplicação
CMD ["uvicorn", "services.api.main:app", "--host", "0.0.0.0", "--port", "8000"]
