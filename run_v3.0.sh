#!/bin/bash
echo "shell call python script"
echo "result_data_pr.py"

python result_data_pr.py  -sf "./331_v3/result_all_v3.0.txt" -pf "process_result_v3.0.txt"
python result_data_pr.py  -sf "./331_v3/result_bg_v3.0.txt" -pf "process_result_v3.0.txt"
python result_data_pr.py  -sf "./331_v3/result_cl_v3.0.txt" -pf "process_result_v3.0.txt"
python result_data_pr.py  -sf "./331_v3/result_nm_v3.0.txt" -pf "process_result_v3.0.txt"



