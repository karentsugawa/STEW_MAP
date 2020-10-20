#%% IMPORT & Get Layers
import geopandas as gpd
import pandas as pd
import fiona

file_path = r"G:\My Drive\STEW-MAP SAVI Mapping\STEW-MAP 2017 Public Data\2017STEWMAP.gdb"

layerlist = fiona.listlayers( file_path )
layerlist
#%% IMpPORT DATA
df = gpd.read_file( file_path , driver="OpenFileGDB" , layer = 'NYC2017_STEWMAP_TURFS_18N_Research'  )
df.sample(5)
# %% ISOLATE SELECTED GROUPS

groups = [ 
    "Citizen Projects",
    "8th Street Block Association",
    "Coney Island Beautification Project, Inc.",
    "Lotus Garden",
    "LUNGS (Loisaida United Neighborhood Gardens)" ,
    "Natural Areas Conservancy",
    "Newtown Creek Alliance",
    "New Yorkers for Parks",
    "New York Botanical Garden",
    "Promenade Garden Conservancy ",
    "Protectors of Pine Oak Woods",
    "Randall's Island Park Alliance",
    "The People's Own Organic Power (POOP) Project",
    "Trout Unlimited - Trout in the Classroom",
    "Warren St. Marks Community Garden",
    "We Run Brownsville"
]

dfg = df[ df['OrgName'].isin(groups) ]
[i for i in sorted(dfg['OrgName'].unique()) ]

#%%

cols = dfg.columns.tolist()

# %%

dfg['OrgName'] = dfg['OrgName'].str.strip()
dfg = dfg[['OrgName','OrgWebSite','Mission','geometry']]
dfg
# %%

dfg.to_file( r'C:\Users\csucuogl\Documents\GitHub\STEW_MAP\group_data\Groups.geojson' , driver="GeoJSON" )

