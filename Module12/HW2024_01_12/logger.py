import os
import logging

log_dir = os.path.dirname(os.path.abspath(__file__))  # Директория текущего файла
log_file = os.path.join(log_dir, 'students.log')

logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    filemode='w',
    format='\n\n%(asctime)s | %(levelname)s | %(message)s', encoding='utf8'
)