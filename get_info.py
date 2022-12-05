from util_commands import list_hw_info, check_list_read_file, read_file, check_list_read_command, check_list_psutil

print("Get info about system from sys file:")
list_hw_info(check_list_read_file)
print("------------------------------\n")

print("Get info use commands:")
list_hw_info(check_list_read_command)
print("------------------------------\n")
print()

print("Get info use psutil:")
list_hw_info(check_list_psutil)
print("------------------------------\n")
