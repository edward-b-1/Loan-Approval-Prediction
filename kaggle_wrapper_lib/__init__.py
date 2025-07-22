import subprocess
import pandas
import io

def string_cli_to_command(string_cli):
    return string_cli.split(' ')

def get_command_kaggle_competition_submit(filename, message):
    command_string = f'kaggle competitions submit -c playground-series-s4e10 -f {filename} -m {message}'
    command = string_cli_to_command(command_string)
    return command

def get_command_kaggle_competition_submissions():
    command_string = 'kaggle competitions submissions playground-series-s4e10 -v'
    command = string_cli_to_command(command_string)
    return command

def kaggle_competition_submit(filename, message):
    command = get_command_kaggle_competition_submit(filename, message)
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    return result

def kaggle_competition_submissions():
    command = get_command_kaggle_competition_submissions()
    
    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=True,
    )
    csv_output = result.stdout
    
    df = pandas.read_csv(io.StringIO(csv_output))
    
    return df
    