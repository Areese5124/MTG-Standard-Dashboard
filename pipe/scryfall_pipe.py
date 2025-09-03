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
  
from dep.Scryfall_API_Functions import call_standard_cards
from dep.Scryfall_API_Functions import standard_cards_check
from dep.Scryfall_API_Functions import json_save
from dep.Snowflake_Login import snowflake_login
from dep.Scryfall_Snowflake_Functions import database_connect
from dep.Scryfall_Snowflake_Functions import creating_json_stage
from dep.Scryfall_Snowflake_Functions import loading_json_into_stage
from dep.Scryfall_Snowflake_Functions import porting_json_data_in
from dep.Scryfall_Snowflake_Functions import parsing_json_into_new_table
from dep.Scryfall_Snowflake_Functions import txt_newest_table
#------------------------------------------------------------------

standard_cards = call_standard_cards()
check = standard_cards_check(standard_cards)

if check:
    new_file_name = json_save(standard_cards)
    cursor = snowflake_login()
    database_connect(cursor)
    stage_name = creating_json_stage(cursor)
    loading_json_into_stage(new_file_name, stage_name, cursor)
    porting_json_data_in(new_file_name, stage_name, cursor)
    parsing_json_into_new_table(stage_name, cursor)
    txt_newest_table(stage_name, cursor)
    cursor.close()
