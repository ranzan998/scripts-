path="/media/scilab/disk_ranjan/works/Rameswaram/shankar_seventh/datasets/1current/rotate/rotate_merged/"
files=sorted([f for f in os.listdir(path) if f.endswith('.nc')])
ds = [xr.open_dataset(path+f) for f in files]

# Define a function to determine the season for each month
def get_season(month):
    if month in [12, 1, 2]:
        return 'DJF'
    elif month in [3, 4, 5]:
        return 'MAM'
    elif month in [6, 7, 8,9]:
        return 'JJAS'
    elif month in [10, 11]:
        return 'ON'

    
# Vectorize the get_season function
vectorized_get_season = np.vectorize(get_season)
names = ["ab","ab_valid","gom","pb","PP","PP_valid"]

# Add a 'season' coordinate to the dataset

df = pd.DataFrame()

c = 0
for f in ds:
    f['season'] = xr.DataArray(vectorized_get_season(f['TAXIS.month']), dims='TAXIS')
    seasonal_mean = f.groupby('season').mean(dim='TAXIS')
    df1 = pd.DataFrame({'season':['DJF',"MAM","JJAS","ON"]},index=[names[c],names[c],names[c],names[c]])

    df1["along_smean"] = seasonal_mean.along_shore[:,0,0].values.round(2)
    df1["cross_smean"] = seasonal_mean.cross_shore[:,0,0].values.round(2)
    df = df.append(df1)  
    c+=1
