def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:

                if not line.strip():
                    continue
                    
                try:
                    _, salary = line.strip().split(',')
                    salary = float(salary)
                    total += salary
                    count += 1
                except ValueError:
                    print(f"Error: Invalid data format in line: {line.strip()}")
                    continue
                    
        if count == 0:
            return 0, 0
            
        average = round(total / count, 2)
        return total, average
        
    except FileNotFoundError:
        print("Error: File not found")
        return 0, 0
    except Exception as e:
        print(f"Error: {e}")
        return 0, 0
    
if __name__ == "__main__":
    total, average = total_salary("salary_file.txt")
    print(f"Total salary: {total}, Average salary: {average}")