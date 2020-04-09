import os, subprocess, sys

current_dir = os.path.split(os.path.realpath(sys.argv[0]))[0]
app_dir = current_dir + '\App\PuTTY'
print(current_dir)
print(app_dir)

config_dir = current_dir + '\Data\Settings\Config'

cmdline = app_dir + '\PuTTY.exe /F "' + config_dir + '"'
# subprocess.Popen(cmdline)
print(config_dir)
print(cmdline)