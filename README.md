# RAG System for Annual Report Question Answering

## Описание

Проект реализует RAG-систему для ответов на вопросы по PDF.
Система извлекает текст из PDF-документов, индексирует его и использует LLM (GigaChat)
строго как экстрактор информации на основе найденного контекста.

LLM не использует внешние знания, не делает выводов и не придумывает ответы.
Если информация отсутствует в тексте, возвращается `N/A` или `False`.

---

## Архитектура

PDF → Parsing → Chunking → TF-IDF + FAISS → Retrieval → LLM (extractor) → submission.json

---

## Зависимости

- Python 3.10+
- pdfplumber
- scikit-learn
- faiss-cpu
- requests

---

## Структура данных

data/
├── pdfs/ # входные PDF-файлы
├── parsed_pages.json # распарсенные страницы
├── chunks.json # текстовые чанки
├── tfidf_vectorizer.pkl # TF-IDF векторизатор
├── faiss.index # FAISS индекс

---

## Инструкция по запуску

Установите зависимости:

pip install -r requirements.txt

Запускайте скрипты строго по порядку:

python pdf_parse.py
python chunking.py
python embed_index.py
python main.py

---

## Настройка GigaChat

В файле `config.py` необходимо указать access token:

---

## Результат

После выполнения `main.py` будет создан файл `submission.json`,
полностью соответствующий требуемому формату сабмишна.