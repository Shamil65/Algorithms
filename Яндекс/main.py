import pandas as pd
import sys

# -----------------------------
# Функция для анализа DataFrame с записью в файл
# -----------------------------
def analyze_df_to_file(df, filename="analysis.txt", name="DataFrame"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n=== Анализ {name} ===\n\n")
        
        # 1. Общая информация
        f.write("1. Общая информация:\n")
        buffer = sys.stdout
        sys.stdout = f
        df.info()
        sys.stdout = buffer
        
        # 2. Размер
        f.write("\n2. Размерность:\n")
        f.write(f"Строк: {df.shape[0]}, Столбцов: {df.shape[1]}\n")
        
        # 3. Первые 5 строк
        f.write("\n3. Первые 5 строк:\n")
        f.write(df.head().to_string())
        f.write("\n")
        
        # 4. Статистика
        f.write("\n4. Статистика колонок:\n")
        f.write(df.describe(include='all').T.to_string())
        f.write("\n")
        
        # 5. Пропуски
        f.write("\n5. Пропуски по столбцам:\n")
        missing = df.isnull().sum()
        missing_percent = (missing / df.shape[0] * 100).round(2)
        missing_df = pd.DataFrame({'missing_count': missing, 'missing_percent': missing_percent})
        f.write(missing_df.sort_values(by='missing_count', ascending=False).to_string())
        f.write("\n")
        
        # 6. Уникальные значения
        f.write("\n6. Уникальные значения по столбцам (топ 5):\n")
        for col in df.columns:
            f.write(f"{col}: {df[col].nunique()} уникальных значений\n")
            if df[col].nunique() <= 5:
                f.write(df[col].value_counts().to_string())
                f.write("\n")
        
        # 7. Дубликаты
        f.write("\n7. Дубликаты строк:\n")
        f.write(str(df.duplicated().sum()) + "\n")
        
        # 8. Бесконечные значения
        f.write("\n8. Бесконечные значения:\n")
        inf_count = df.replace([float('inf'), -float('inf')], pd.NA).isna().sum()
        inf_count = inf_count[inf_count > 0]
        f.write(inf_count.to_string() + "\n")
        
        # 9. Случайные примеры
        f.write("\n9. Примеры значений в строках:\n")
        f.write(df.sample(5, random_state=42).to_string())
        f.write("\n\n")
        
    print(f"Анализ {name} сохранён в {filename}")

# -----------------------------
# Загрузка файлов
# -----------------------------
train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")

# -----------------------------
# Очистка файла перед записью
# -----------------------------
with open("analysis.txt", "w", encoding="utf-8") as f:
    f.write("Анализ CSV файлов\n==================\n")

# -----------------------------
# Анализ файлов
# -----------------------------
analyze_df_to_file(train, "analysis.txt", "train.csv")
analyze_df_to_file(test, "analysis.txt", "test.csv")
