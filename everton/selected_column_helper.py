# Pipeline for treating nan values and applying PCA to different information levels:
from .utils import  *

# Updating dtypes_dict:
new_dtypes_dict = dtypes_dict.copy()
new_dtypes_dict['AGER_TYP'] = 'cat'
new_dtypes_dict['D19_GESAMT_ANZ_24'] = 'num'
new_dtypes_dict['D19_GESAMT_DATUM'] = 'num'
new_dtypes_dict['D19_GESAMT_OFFLINE_DATUM'] = 'num'
new_dtypes_dict['D19_GESAMT_ONLINE_DATUM'] = 'num'
new_dtypes_dict['D19_KONSUMTYP'] = 'cat'
new_dtypes_dict['D19_KONSUMTYP_MAX'] = 'num'
new_dtypes_dict['D19_SONSTIGE'] = 'num'
new_dtypes_dict['D19_SOZIALES'] = 'num'
new_dtypes_dict['D19_VERSAND_DATUM'] = 'num'
new_dtypes_dict['D19_VERSAND_OFFLINE_DATUM'] = 'num'
new_dtypes_dict['D19_VOLLSORTIMENT'] = 'num'
new_dtypes_dict['EXTSEL992'] = 'num'
new_dtypes_dict['GEBURTSJAHR'] = 'num'



# Updating info_level dictionary:
new_info_level = info_level.copy()

# Adding columns:
# Person:
new_info_level['person'].append('AGER_TYP')
new_info_level['person'].append('GEBURTSJAHR')

# Household:
new_info_level['household'].append('D19_GESAMT_ANZ_24')
new_info_level['household'].append('D19_GESAMT_DATUM')
new_info_level['household'].append('D19_GESAMT_OFFLINE_DATUM')
new_info_level['household'].append('D19_GESAMT_ONLINE_DATUM')
new_info_level['household'].append('D19_KONSUMTYP')
new_info_level['household'].append('D19_KONSUMTYP_MAX')
new_info_level['household'].append('D19_SONSTIGE')
new_info_level['household'].append('D19_SOZIALES')
new_info_level['household'].append('D19_VERSAND_DATUM')
new_info_level['household'].append('D19_VERSAND_OFFLINE_DATUM')
new_info_level['household'].append('D19_VOLLSORTIMENT')

# Macrocell:
new_info_level['macrocell'].append('EXTSEL992')

#%%

# Dividing Person features into numerical, categorical and binary:
pers_num_features = list()

pers_cat_features = list()

pers_bin_features = list()

# Adding columns to lists:
for pers_col in new_info_level['person']:
    try:
        dtype = new_dtypes_dict[pers_col]
    except:
        dtype = new_feat_dtypes_dict[pers_col]

    if dtype == 'num':
        pers_num_features.append(pers_col)
    elif dtype == 'cat':
        pers_cat_features.append(pers_col)
    else:
        pers_bin_features.append(pers_col)

#%%

# Dividing Household features into numerical, categorical and binary:
hh_num_features = list()

hh_cat_features = list()

hh_bin_features = list()

# Adding columns to lists:
for hh_col in new_info_level['household']:
    try:
        dtype = new_dtypes_dict[hh_col]
    except:
        dtype = new_feat_dtypes_dict[hh_col]

    if dtype == 'num':
        hh_num_features.append(hh_col)
    elif dtype == 'cat':
        hh_cat_features.append(hh_col)
    else:
        hh_bin_features.append(hh_col)

#%%

# Dividing Microcell features into numerical, categorical and binary:
mic_num_features = list()

mic_cat_features = list()

mic_bin_features = list()

# Adding columns to lists:
for mic_col in new_info_level['microcell']:
    try:
        dtype = new_dtypes_dict[mic_col]
    except:
        dtype = new_feat_dtypes_dict[mic_col]

    if dtype == 'num':
        mic_num_features.append(mic_col)
    elif dtype == 'cat':
        mic_cat_features.append(mic_col)
    else:
        mic_bin_features.append(mic_col)

#%%

# Dividing Macrocell features into numerical, categorical and binary:
mac_num_features = list()

mac_cat_features = list()

mac_bin_features = list()

# Adding columns to lists:
for mac_col in new_info_level['macrocell']:
    try:
        dtype = new_dtypes_dict[mac_col]
    except:
        dtype = new_feat_dtypes_dict[mac_col]

    if dtype == 'num':
        mac_num_features.append(mac_col)
    elif dtype == 'cat':
        mac_cat_features.append(mac_col)
    else:
        mac_bin_features.append(mac_col)

#%%

# Dividing Community features into numerical, categorical and binary:
com_num_features = list()

com_cat_features = list()

com_bin_features = list()

# Adding columns to lists:
for com_col in new_info_level['community']:
    try:
        dtype = new_dtypes_dict[com_col]
    except:
        dtype = new_feat_dtypes_dict[com_col]

    if dtype == 'num':
        com_num_features.append(com_col)
    elif dtype == 'cat':
        com_cat_features.append(com_col)
    else:
        com_bin_features.append(com_col)


# Concatenating selected columns:
selected_columns = pers_num_features + pers_cat_features + pers_bin_features + hh_num_features + hh_cat_features + mic_num_features + mic_cat_features + mic_bin_features + mac_num_features + mac_cat_features + mac_bin_features + com_num_features