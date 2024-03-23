def total_salary(path):
    total = 0
    count = 0
    with open(path, 'r') as data:
        for line in data:
            salary = float(line.strip())
            total += salary
            count += 1
    average = total / count if count > 0 else 0
    return [total, average]
total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")