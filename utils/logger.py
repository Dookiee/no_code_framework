import os
import datetime

import ipdb

from test_reusables.service.logger_level import LogLevel

# declaring this globally so that it gets initialised only once for all
current_time = datetime.datetime.now().strftime('%d%m%Y-%H-%M')
print('Find logs in test_reports/logs-' + current_time)


def log(text, log_level):
    """
    To write logs in the respective log files
    """
    if log_level.value >= LogLevel[os.environ['log_level']].value and log_level.value != 1:
        log_file_path = get_log_file_path()
        text = datetime.datetime.now().isoformat() + '\t' + log_level.name + '\t' + str(text) + '\n'
        file_object = open(log_file_path, 'a')
        file_object.write(text)
        file_object.close()


def get_log_file_path():
    """
    To create log directories in test_reports folder
    """
    log_dir_path = 'test_reports/logs-' + current_time
    create_log_dir_if_not_exists(log_dir_path)
    try:
        log_dir_path = get_log_file_directory(log_dir_path)
        file_path = log_dir_path + '/' + get_log_file_name()
    except AttributeError as e:
        file_path = log_dir_path + '/' + 'setup.log'
    create_log_dir_if_not_exists(log_dir_path)
    return file_path


def create_log_dir_if_not_exists(log_dir_path):
    try:
        if not os.path.exists(log_dir_path):
            os.mkdir(log_dir_path)
    except FileExistsError:
        print('dir ' + log_dir_path + ' already exists!')


def get_log_file_directory(log_folder_path):
    """
    To get the current log directory
    """
    node_id = os.environ.get('PYTEST_CURRENT_TEST').split(' (')[0]
    node_items = node_id.split('::')
    dir_name = node_items[0].split('/')
    if 'test_cases' in dir_name:
        dir_name = log_folder_path + '/' + dir_name[2] + '-' + dir_name[3] + '-' + dir_name[4].split('.')[0]
    elif 'test_data' in dir_name:
        dir_name = log_folder_path + '/' + dir_name[1].split('.')[0]
    else:
        dir_name = log_folder_path + '/' + dir_name[1] + '-' + dir_name[2].split('.')[0]
    return dir_name


def get_log_file_name():
    """
    To get the current log file path
    """
    node_id = os.environ.get('PYTEST_CURRENT_TEST').split(' (')[0]
    node_items = node_id.split('::')
    log_file_name = node_items[-1]
    log_file_name = log_file_name.replace('/', '_')
    log_file_name = log_file_name.replace('’', '_')
    if len(log_file_name) > 200:
        log_file_name = log_file_name[:200]
    log_file_name = log_file_name + '.log'
    return log_file_name
