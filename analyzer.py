file_path = "simulation.log"

error_count = 0
warning_count = 0
info_count = 0

with open(file_path, "r") as file:
    lines = file.readlines()


for line in lines:
    if "ERROR" in line:
        error_count += 1
    elif "WARNING" in line:
        warning_count += 1
    elif "INFO" in line:
        info_count += 1


status = "PASS"
if error_count > 0:
    status = "FAIL"


print("----- Log Summary -----")
print(f"Errors   : {error_count}")
print(f"Warnings : {warning_count}")
print(f"Info     : {info_count}")
print(f"Status   : {status}")
