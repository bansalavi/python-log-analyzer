file_path = "simulation.log"
report_path = "report.txt"

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

summary = (
    "----- Log Summary -----\n"
    f"Errors   : {error_count}\n"
    f"Warnings : {warning_count}\n"
    f"Info     : {info_count}\n"
    f"Status   : {status}\n"
)

print(summary)

with open(report_path, "w") as report:
    report.write(summary)

print("Report saved as report.txt")
