# -*- coding: utf-8 -*-
"""
Created on Sat Jun 28 14:51:01 2025

@author: Arees
"""
#Boiler Plate
import sys
from pathlib import Path
main_dir = str(Path(__file__).parent.parent)
sys.path.append(main_dir)

from dep.standard_function import call_standard_cards
from dep.standard_function import standard_cards_check
from dep.standard_function import json_save
from dep.snowflake_login import snowflake_login
from dep.snowflake_functions import database_connect
from dep.snowflake_functions import create_stage
from dep.snowflake_functions import loading_json_into_stage
from dep.snowflake_functions import porting_json_data_in
from dep.snowflake_functions import parsing_json_into_new_table

#------------------------------------------------------------------

standard_cards = call_standard_cards()
check = standard_cards_check(standard_cards)

check = True
if check:
    new_file_name = json_save(standard_cards)
    cursor = snowflake_login()
    database_connect(cursor)
    stage_name = create_stage(cursor)
    loading_json_into_stage(new_file_name, stage_name, cursor)
    porting_json_data_in(new_file_name, stage_name, cursor)
    parsing_json_into_new_table(stage_name, cursor)
    
    
