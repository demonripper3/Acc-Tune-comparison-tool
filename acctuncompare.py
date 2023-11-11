import json
from deepdiff import DeepDiff
from tkinter import filedialog
from tkinter import Tk

def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def select_json_file():
    root = Tk()
    root.withdraw()  # to hide the small tk window
    file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    return file_path

def remove_keys(obj, keys_to_remove):
    if isinstance(obj, dict):
        return {k: remove_keys(v, keys_to_remove) for k, v in obj.items() if k not in keys_to_remove}
    elif isinstance(obj, list):
        return [remove_keys(element, keys_to_remove) for element in obj]
    return obj

def calculate_ticks(differences):
    tick_value = 1  # Define the value of one tick
    cheat_threshold = 20  # Define the threshold for cheat warning
    for diff_type, changes in differences.items():
        if diff_type in ['values_changed', 'type_changes']:
            for key in changes:
                old_value = changes[key]['old_value']
                new_value = changes[key]['new_value']
                if isinstance(old_value, (int, float)) and isinstance(new_value, (int, float)):
                    change_in_ticks = round((new_value - old_value) / tick_value)
                    print(f"{key}: Change of {change_in_ticks} ticks")
                    if abs(change_in_ticks) > cheat_threshold:
                        print(f"CHEAT WARNING: {key} changed by more than {cheat_threshold} ticks!")

def compare_json_files(file1, file2):
    keys_to_remove = ['staticCamber', 'toeOutLinear', 'fuelPerLap', 'rodLength', 'strategy']
    
    json1 = remove_keys(load_json(file1), keys_to_remove)
    json2 = remove_keys(load_json(file2), keys_to_remove)

    return DeepDiff(json1, json2, ignore_order=True, significant_digits=3)

def main():
    print("Select the first JSON file.")
    file1 = select_json_file()

    print("Select the second JSON file.")
    file2 = select_json_file()

    differences = compare_json_files(file1, file2)

    print("Differences in Ticks:")
    calculate_ticks(differences)

    input("Press Enter to exit...")  # This line will keep the terminal open

if __name__ == "__main__":
    main()
