def get_cats_info(path):
    cats_info = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                cat_data = line.strip().split(',')
                if len(cat_data) == 3:
                    cat_dict = {
                        "id": cat_data[0],
                        "name": cat_data[1],
                        "age": cat_data[2]
                    }
                    cats_info.append(cat_dict)
    except FileNotFoundError:
        print(f"File '{path}' not found")
        return cats_info
    except Exception as e:
        print(f"Error: {e}")
        return cats_info
    
    return cats_info

if __name__ == "__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)