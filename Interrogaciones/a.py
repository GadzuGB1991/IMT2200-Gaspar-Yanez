import geopandas as gpd
import pandas as pd

def load_data():
    # Load the GeoJSON file using geopandas
    gdf = gpd.read_file('all_pokemon.json')
    
    # Convert to a pandas DataFrame
    df = pd.DataFrame(gdf)
    
    return df

load_data()