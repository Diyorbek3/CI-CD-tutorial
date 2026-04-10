FROM python:3.11-slim
WORKDIR /app
RUN pip install pyTelegramBotAPI
COPY bot.py .
CMD ["python", "bot.py"]