#!/bin/bash
echo "shell call python script"
echo "result_data_pr.py"

python result_data_pr.py  -sf "./4.2_v4/result_all_orig.txt" -pf "process_result_v4.0.txt"
python result_data_pr.py  -sf "./4.2_v4/result_bg_orig.txt" -pf "process_result_v4.0.txt"
python result_data_pr.py  -sf "./4.2_v4/result_cl_orig.txt" -pf "process_result_v4.0.txt"
python result_data_pr.py  -sf "./4.2_v4/result_nm_orig.txt" -pf "process_result_v4.0.txt"



