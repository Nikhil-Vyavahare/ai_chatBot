from datetime import date, datetime
import os


def file_w(text):
    todaydate = datetime.today().strftime("%Y-%m-%d")  # Format date for directory
    now = datetime.now()
    current_time = now.strftime("%H-%M-%S")

    # Create directory if it doesn't exist
    dir_path = f'outputhistory/{todaydate}'
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    file_path = os.path.join(dir_path, f'{current_time}.txt')
    with open(file_path, 'w') as f:
        f.writelines(text)

    print(f'Saved to {file_path}')
