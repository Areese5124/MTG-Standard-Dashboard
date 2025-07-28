# -*- coding: utf-8 -*
"""
Created on Fri Jul 11 11:33:27 2025

@author: Arees
"""
def database_connect (cursor):
    cursor.execute('USE WAREHOUSE COMPUTE_WH')
    print('Connected to Warehouse')
    cursor.execute('USE DATABASE STANDARD_PLAYABLE_DATASET')
    print('Connected to Database')
    cursor.execute('USE SCHEMA STANDARD_PLAYABLE_DATASET.DATA_REPO')
    print('Connected to Schema')
    
def create_stage (cursor):
    from datetime import date
    date = (str(date.today())).replace('-','_')
    stage_name = 'standard_cards_' + date
    cursor.execute(
        "CREATE OR REPLACE STAGE %s FILE_FORMAT=(TYPE='json')"
        %(stage_name,) 
                   )
    print('New stage %s created' %(stage_name,) )
    return (stage_name)

def loading_json_into_stage(file, stage, cursor):
    from pathlib import Path
    current_dir = Path.cwd()
    most_recent_loc = ((current_dir / '..' / 'data' / file).resolve())
    most_recent_loc = str(most_recent_loc).replace('\\','/')
    cursor.execute(
        "PUT 'file://%s' @%s"
        %(most_recent_loc, stage)
        ) 
    print('Successfully put %s into the stage %s' % (file, stage))

def porting_json_data_in (file, stage, cursor): 
    cursor.execute(
        'CREATE OR REPLACE TEMPORARY TABLE json_basic_code (json_data VARIANT)'
        )
    cursor.execute(
        '''
        COPY INTO json_basic_code 
        FROM @%s/%s.gz
        FILE_FORMAT = (format_name = json_format)
        '''
        %(stage, file)
        )
    print(
        '''Successfully moved the %s data from the %s stage
          into the temporary table.
          ''' % (file, stage))
          
def parsing_json_into_new_table(stage, cursor):
    cursor.execute(
        '''
        CREATE OR REPLACE TABLE %s AS SELECT 
            json_data:name::string as Card_Name,
            json_data:cmc::float AS Converted_Mana_Cost,
            json_data:mana_cost::string as Mana_Cost,
            json_data:color_identity AS Color_Identity,
            json_data:colors AS Colors,
            json_data:keywords AS Keywords,
            json_data:oracle_text::string as Card_Text,
            json_data:power::string as Power,
            json_data:toughness::string as Toughness,
            json_data:type_line::string as Type_Line,
            json_data:set_name::string as Set_Name
        FROM json_basic_code
        ;
        '''
        %(stage,)
        )
    
    
    