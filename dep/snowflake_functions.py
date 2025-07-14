# -*- coding: utf-8 -*-
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
        "CREATE STAGE %s FILE_FORMAT=(TYPE='json')"
        %(stage_name,) 
                   )
    print('New stage %s created' %(stage_name,) )
    return (stage_name)

def loading_json_into_stage(file, stage, cursor):
    from pathlib import Path
    current_dir = Path(__file__).parent
    most_recent_loc = ((current_dir / '..' / 'data' / file).resolve())
    most_recent_loc = str(most_recent_loc).replace('\\','/')
    cursor.execute(
        "PUT 'file://%s' @%s"
        %(most_recent_loc, stage)
        )
    print('Successfully put %s into the stage %s' % (file, stage))

def porting_json_data_in (cursor): 
    cursor.execute(
        'CREATE OR REPLACE TRANSIENT TABLE json_basic_code (json_data VARIANT)'
        )
    cursor.execute(
        '''
        COPY INTO json_basic_code FROM @standard_cards_2025_07_11
        FILE_FORMAT=(TYPE='json')
        FILES = ('standard-cards-2025-07-11.json.gz')
        '''
        )
    
    
    
    