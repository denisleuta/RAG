import json

def convert_page_to_index(file_path, output_path=None):
    # Читаем JSON файл
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Рекурсивно заменяем "page" на "page_index"
    def replace_keys(obj):
        if isinstance(obj, dict):
            new_dict = {}
            for key, value in obj.items():
                if key == "page":
                    new_dict["page_index"] = value
                else:
                    new_dict[key] = replace_keys(value)
            return new_dict
        elif isinstance(obj, list):
            return [replace_keys(item) for item in obj]
        else:
            return obj
    
    # Применяем замену
    converted_data = replace_keys(data)
    
    # Сохраняем результат
    if output_path is None:
        output_path = file_path.replace('.json', '_converted.json')
    
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(converted_data, f, indent=2, ensure_ascii=False)
    
    print(f"Конвертация завершена. Результат сохранен в: {output_path}")
    return converted_data

# Использование:
convert_page_to_index('submission.json', 'submission.json')