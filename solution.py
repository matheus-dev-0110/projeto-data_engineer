import pandas as pd
import numpy as np

def all_pet_data(activities_file, health_file, users_file):
    activities = pd.read_csv(activities_file)
    health = pd.read_csv(health_file)
    users = pd.read_csv(users_file)

    activity_map = {
        'Walking': 'Walking', 'Walk': 'Walking',
        'Playing': 'Playing', 'Play': 'Playing',
        'Resting': 'Resting', 'Rest': 'Resting',
    }
    activities['activity_type'] = activities['activity_type'].astype(str).str.strip().map(activity_map)
    activities['date'] = pd.to_datetime(activities['date'], errors='coerce')

    activities['duration_minutes'] = pd.to_numeric(
        activities['duration_minutes'].astype(str).str.replace('-', '', regex=False).str.strip(),
        errors='coerce'
    )

    activities['issue'] = np.nan
    activities['resolution'] = np.nan
    df_activities = activities[['pet_id', 'date', 'activity_type', 'duration_minutes', 'issue', 'resolution']].copy()

    health = health.rename(columns={'visit_date': 'date'})
    health['date'] = pd.to_datetime(health['date'], errors='coerce')
    health['activity_type'] = 'Health'
    health['duration_minutes'] = 0

    for col in ['issue', 'resolution']:
        health[col] = health[col].astype(str).str.strip()
        health[col] = health[col].replace({'Nan': np.nan, 'None': np.nan, 'nan': np.nan, '': np.nan})

    df_health = health[['pet_id', 'date', 'activity_type', 'duration_minutes', 'issue', 'resolution']].copy()

    df = pd.concat([df_activities, df_health], ignore_index=True)
    df = df.dropna(subset=['pet_id', 'date'])
    df['pet_id'] = df['pet_id'].astype(int)

    users['owner_age_group'] = users['owner_age_group'].astype(str).str.strip().replace(
        {'Nan': np.nan, 'None': np.nan, 'nan': np.nan, '': np.nan}
    )
    users['pet_type'] = users['pet_type'].astype(str).str.strip().str.title().replace(
        {'Nan': np.nan, 'None': np.nan, 'nan': np.nan, '': np.nan}
    )

    users = users[['owner_id', 'pet_id', 'owner_age_group', 'pet_type']].copy()
    users['owner_id'] = users['owner_id'].astype(int)
    users['pet_id'] = users['pet_id'].astype(int)

    df = df.merge(users, on='pet_id', how='left')
    df = df.dropna(subset=['owner_id'])
    df['owner_id'] = df['owner_id'].astype(int)

    df = df[['pet_id', 'date', 'activity_type', 'duration_minutes',
              'issue', 'resolution', 'owner_id', 'owner_age_group', 'pet_type']]

    df['duration_minutes'] = pd.to_numeric(df['duration_minutes'], errors='coerce')

    return df
