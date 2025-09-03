# -*- coding: utf-8 -*-
"""
Created on Fri Aug 29 11:31:54 2025

@author: Arees
"""
def database_connect (cursor):
    cursor.execute('USE WAREHOUSE COMPUTE_WH')
    print('Connected to Warehouse')
    cursor.execute('USE DATABASE STANDARD_PLAYABLE_DATASET')
    print('Connected to Database')
    cursor.execute('USE SCHEMA STANDARD_PLAYABLE_DATASET.DATA_REPO')
    print('Connected to Schema')

def average_deck_makeup_creating_json_stage(cursor):
    from datetime import date
    date = (str(date.today())).replace('-','_')
    stage_name = 'average_deck_makeup_' + date
    cursor.execute(
        "CREATE STAGE IF NOT EXISTS %s FILE_FORMAT=(TYPE='json')"
        %(stage_name,) 
                   )
    print('New stage %s created' %(stage_name,) )
    return (stage_name)

def loading_average_deck_makeup_json_into_stage(file, stage, cursor):
    from pathlib import Path
    current_dir = Path.cwd()
    most_recent_loc = ((current_dir / '..' / 'Data/Archetype-Analysis' / file).resolve())
    most_recent_loc = str(most_recent_loc).replace('\\','/')
    cursor.execute(
        "PUT 'file://%s' @%s"
        %(most_recent_loc, stage)
        )                
    print('Successfully put %s into the stage %s' % (file, stage))

