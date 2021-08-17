import numpy as np
import pandas as pd
import pickle
# Mapping unknown values by variable:
unknown_dict = {'CAMEO_DEU_2015': ['XX'], 'CAMEO_INTL_2015': ['XX'], 'CAMEO_DEUG_2015': ['X'], 'AGER_TYP': [-1, 0],
                'ALTER_HH': [0], 'ARBEIT': [9], 'D19_BANKEN_ANZ_12': [0], 'D19_BANKEN_ANZ_24': [0], 'D19_BANKEN_DATUM': [10],
                'D19_BANKEN_DIREKT': [0], 'D19_BANKEN_GROSS': [0], 'D19_BANKEN_LOKAL': [0], 'D19_BANKEN_OFFLINE_DATUM': [10],
                'D19_BANKEN_ONLINE_DATUM': [10], 'D19_BANKEN_ONLINE_QUOTE_12': [0, 10], 'D19_BANKEN_REST': [0],
                'D19_BEKLEIDUNG_GEH': [0], 'D19_BEKLEIDUNG_REST': [0], 'D19_BILDUNG': [0], 'D19_BIO_OEKO': [0],
                'D19_BUCH_CD': [0], 'D19_DIGIT_SERV': [0], 'D19_DROGERIEARTIKEL': [0], 'D19_ENERGIE': [0], 'D19_FREIZEIT': [0],
                'D19_GARTEN': [0], 'D19_GESAMT_ANZ_12': [0], 'D19_GESAMT_ANZ_24': [0], 'D19_GESAMT_DATUM': [10],
                'D19_GESAMT_OFFLINE_DATUM': [10], 'D19_GESAMT_ONLINE_DATUM': [10], 'D19_GESAMT_ONLINE_QUOTE_12': [0,10],
                'D19_HANDWERK': [0], 'D19_HAUS_DEKO': [0], 'D19_KINDERARTIKEL': [0], 'D19_KONSUMTYP': [9],
                'D19_KONSUMTYP_MAX': [8, 9], 'D19_KOSMETIK': [0], 'D19_LEBENSMITTEL': [0], 'D19_LOTTO': [0],
                'D19_SOZIALES': [0], 'D19_NAHRUNGSERGAENZUNG': [0], 'D19_RATGEBER': [0], 'D19_REISEN': [0],
                'D19_SAMMELARTIKEL': [0], 'D19_SCHUHE': [0], 'D19_SONSTIGE': [0], 'D19_TECHNIK': [0], 'D19_TELKO_ANZ_12': [0],
                'D19_TELKO_ANZ_24': [0], 'D19_TELKO_DATUM': [10], 'D19_TELKO_MOBILE': [0], 'D19_TELKO_OFFLINE_DATUM': [10],
                'D19_TELKO_ONLINE_DATUM': [10], 'D19_TELKO_ONLINE_QUOTE_12': [0, 10], 'D19_VERSAND_ONLINE_QUOTE_12': [0, 10],
                'D19_VERSI_ONLINE_QUOTE_12': [0, 10], 'D19_TELKO_REST': [0], 'D19_TIERARTIKEL': [0], 'D19_VERSAND_ANZ_12': [0],
                'D19_VERSAND_ANZ_24': [0], 'D19_VERSAND_DATUM': [10], 'D19_VERSAND_OFFLINE_DATUM': [10],
                'D19_VERSAND_ONLINE_DATUM': [10], 'D19_VERSAND_REST': [0], 'D19_VERSI_ANZ_12': [0], 'D19_VERSI_ANZ_24': [0],
                'D19_VERSI_DATUM': [10], 'D19_VERSI_OFFLINE_DATUM': [10], 'D19_VERSI_ONLINE_DATUM': [10],
                'D19_VERSICHERUNGEN': [0], 'D19_VOLLSORTIMENT': [0], 'D19_WEIN_FEINKOST': [0], 'GEBURTSJAHR': [0],
                'HEALTH_TYP': [-1], 'KBA05_ALTER1': [9], 'KBA05_ALTER2': [9], 'KBA05_ALTER3': [9], 'KBA05_ALTER4': [9],
                'KBA05_ANHANG': [9], 'KBA05_AUTOQUOT': [9], 'KBA05_BAUMAX': [0], 'KBA05_CCM1': [9], 'KBA05_CCM2': [9],
                'KBA05_CCM3': [9], 'KBA05_CCM4': [9], 'KBA05_DIESEL': [9], 'KBA05_FRAU': [9], 'KBA05_HERST1': [9],
                'KBA05_HERST2': [9], 'KBA05_HERST3': [9], 'KBA05_HERST4': [9], 'KBA05_HERST5': [9], 'KBA05_HERSTTEMP': [9],
                'KBA05_KRSAQUOT': [9], 'KBA05_KRSHERST1': [9], 'KBA05_KRSHERST2': [9], 'KBA05_KRSHERST3': [9],
                'KBA05_KRSKLEIN': [9], 'KBA05_KRSOBER': [9], 'KBA05_KRSVAN': [9], 'KBA05_KRSZUL': [9], 'KBA05_KW1': [9],
                'KBA05_KW2': [9], 'KBA05_KW3': [9], 'KBA05_MAXAH': [9], 'KBA05_MAXBJ': [9], 'KBA05_MAXHERST': [9],
                'KBA05_MAXSEG': [9], 'KBA05_MAXVORB': [9], 'KBA05_MOD1': [9], 'KBA05_MOD2': [9], 'KBA05_MOD3': [9],
                'KBA05_MOD4': [9], 'KBA05_MOD8': [9], 'KBA05_MODTEMP': [6], 'KBA05_MOTOR': [9], 'KBA05_MOTRAD': [9],
                'KBA05_SEG1': [9], 'KBA05_SEG10': [9], 'KBA05_SEG2': [9], 'KBA05_SEG3': [9], 'KBA05_SEG4': [9],
                'KBA05_SEG5': [9], 'KBA05_SEG6': [9], 'KBA05_SEG7': [9], 'KBA05_SEG8': [9], 'KBA05_SEG9': [9],
                'KBA05_VORB0': [9], 'KBA05_VORB1': [9], 'KBA05_VORB2': [9], 'KBA05_ZUL1': [9], 'KBA05_ZUL2': [9],
                'KBA05_ZUL3': [9], 'KBA05_ZUL4': [9], 'KKK': [0], 'KOMBIALTER': [9], 'LP_LEBENSPHASE_FEIN': [0],
                'LP_LEBENSPHASE_GROB': [0], 'NATIONALITAET_KZ': [0], 'ORTSGR_KLS9': [0], 'PRAEGENDE_JUGENDJAHRE': [0],
                'REGIOTYP': [0], 'RELAT_AB': [9], 'RT_UEBERGROESSE': [0], 'SHOPPER_TYP': [-1], 'TITEL_KZ': [0],
                'VERS_TYP': [-1], 'W_KEIT_KIND_HH': [0], 'WOHNLAGE': [0], 'ALTERSKATEGORIE_GROB': [9]}

# Organizing dataframe structure (column dtypes and adding together unknown and nan values):
def join_nan_with_unknown(df, unknown = unknown_dict):
    '''
    It maps unknown values by column and transform them to nan values.

    Input:
    df: original dataframe;
    unkown: dictionary mapping columns and their respective known values' classes.

    Output:
    df: transformed dataframe.
    '''
    # Looping through columns with unkown values:
    for col in list(unknown.keys()):
        df[col] = [np.nan if df[col].iloc[i] in unknown[col] else df[col].iloc[i] for i in range(df.shape[0])]

    return df

# Mapping dtypes by variable:
dtypes_dict = {'AKT_DAT_KL': 'num', 'ALTER_HH': 'num', 'ALTERSKATEGORIE_FEIN': 'num', 'ANZ_HAUSHALTE_AKTIV': 'num',
               'ANZ_HH_TITEL': 'num', 'ANZ_KINDER': 'num', 'ANZ_PERSONEN': 'num', 'ANZ_STATISTISCHE_HAUSHALTE': 'num',
               'ANZ_TITEL': 'num', 'ARBEIT': 'num', 'BALLRAUM': 'num', 'CAMEO_DEU_2015': 'cat', 'CAMEO_DEUG_2015': 'num',
               'CAMEO_INTL_2015': 'num', 'CJT_GESAMTTYP': 'cat', 'CJT_KATALOGNUTZER': 'num', 'CJT_TYP_1': 'num',
               'CJT_TYP_2': 'num', 'CJT_TYP_3': 'num', 'CJT_TYP_4': 'num', 'CJT_TYP_5': 'num', 'CJT_TYP_6': 'num',
               'D19_LETZTER_KAUF_BRANCHE': 'cat', 'DSL_FLAG': 'bin', 'EWDICHTE': 'num', 'FINANZ_ANLEGER': 'num',
               'FINANZ_HAUSBAUER': 'num', 'FINANZ_MINIMALIST': 'num', 'FINANZ_SPARER': 'num', 'FINANZ_UNAUFFAELLIGER': 'num',
               'FINANZ_VORSORGER': 'num', 'FINANZTYP': 'cat', 'FIRMENDICHTE': 'num', 'GEBAEUDETYP': 'cat',
               'GEBAEUDETYP_RASTER': 'num', 'GEMEINDETYP': 'cat', 'GFK_URLAUBERTYP': 'cat', 'GREEN_AVANTGARDE': 'bin',
               'HEALTH_TYP': 'cat', 'HH_DELTA_FLAG': 'bin', 'HH_EINKOMMEN_SCORE': 'num', 'INNENSTADT': 'num',
               'KBA05_ALTER1': 'num', 'KBA05_ALTER2': 'num', 'KBA05_ALTER3': 'num', 'KBA05_ALTER4': 'num',
               'KBA05_ANHANG': 'num', 'KBA05_ANTG1': 'num', 'KBA05_ANTG2': 'num', 'KBA05_ANTG3': 'num', 'KBA05_ANTG4': 'num',
               'KBA05_AUTOQUOT': 'num', 'KBA05_CCM1': 'num', 'KBA05_CCM2': 'num', 'KBA05_CCM3': 'num', 'KBA05_CCM4': 'num',
               'KBA05_DIESEL': 'num', 'KBA05_FRAU': 'num', 'KBA05_GBZ': 'num', 'KBA05_HERST1': 'num', 'KBA05_HERST2': 'num',
               'KBA05_HERST3': 'num', 'KBA05_HERST4': 'num', 'KBA05_HERST5': 'num', 'KBA05_HERSTTEMP': 'cat',
               'KBA05_KRSAQUOT': 'num', 'KBA05_KRSHERST1': 'num', 'KBA05_KRSHERST2': 'num', 'KBA05_KRSHERST3': 'num',
               'KBA05_KRSKLEIN': 'num', 'KBA05_KRSOBER': 'num', 'KBA05_KRSVAN': 'num', 'KBA05_KRSZUL': 'num',
               'KBA05_KW1': 'num', 'KBA05_KW2': 'num', 'KBA05_KW3': 'num', 'KBA05_MAXAH': 'num', 'KBA05_MAXBJ': 'num',
               'KBA05_MAXHERST': 'cat', 'KBA05_MAXSEG': 'num', 'KBA05_MAXVORB': 'num', 'KBA05_MOD1': 'num',
               'KBA05_MOD2': 'num', 'KBA05_MOD3': 'num', 'KBA05_MOD4': 'num', 'KBA05_MOD8': 'num', 'KBA05_MODTEMP': 'cat',
               'KBA05_MOTOR': 'num', 'KBA05_MOTRAD': 'num', 'KBA05_SEG1': 'num', 'KBA05_SEG10': 'num', 'KBA05_SEG2': 'num',
               'KBA05_SEG3': 'num', 'KBA05_SEG4': 'num', 'KBA05_SEG5': 'num', 'KBA05_SEG6': 'num', 'KBA05_SEG7': 'num',
               'KBA05_SEG8': 'num', 'KBA05_SEG9': 'num', 'KBA05_VORB0': 'num', 'KBA05_VORB1': 'num', 'KBA05_VORB2': 'num',
               'KBA05_ZUL1': 'num', 'KBA05_ZUL2': 'num', 'KBA05_ZUL3': 'num', 'KBA05_ZUL4': 'num',
               'KBA13_ALTERHALTER_30': 'num', 'KBA13_ALTERHALTER_45': 'num', 'KBA13_ALTERHALTER_60': 'num',
               'KBA13_ALTERHALTER_61': 'num', 'KBA13_ANTG1': 'num', 'KBA13_ANTG2': 'num', 'KBA13_ANTG3': 'num',
               'KBA13_ANTG4': 'num', 'KBA13_ANZAHL_PKW': 'num', 'KBA13_AUDI': 'num', 'KBA13_AUTOQUOTE': 'num',
               'KBA13_BAUMAX': 'num', 'KBA13_BJ_1999': 'num', 'KBA13_BJ_2000': 'num', 'KBA13_BJ_2004': 'num',
               'KBA13_BJ_2006': 'num', 'KBA13_BJ_2008': 'num', 'KBA13_BJ_2009': 'num', 'KBA13_BMW': 'num',
               'KBA13_CCM_0_1400': 'num', 'KBA13_CCM_1000': 'num', 'KBA13_CCM_1200': 'num', 'KBA13_CCM_1400': 'num',
               'KBA13_CCM_1401_2500': 'num', 'KBA13_CCM_1500': 'num', 'KBA13_CCM_1600': 'num', 'KBA13_CCM_1800': 'num',
               'KBA13_CCM_2000': 'num', 'KBA13_CCM_2500': 'num', 'KBA13_CCM_2501': 'num', 'KBA13_CCM_3000': 'num',
               'KBA13_CCM_3001': 'num', 'KBA13_FAB_ASIEN': 'num', 'KBA13_FAB_SONSTIGE': 'num', 'KBA13_FIAT': 'num',
               'KBA13_FORD': 'num', 'KBA13_GBZ': 'num', 'KBA13_HALTER_20': 'num', 'KBA13_HALTER_25': 'num',
               'KBA13_HALTER_30': 'num', 'KBA13_HALTER_35': 'num', 'KBA13_HALTER_40': 'num', 'KBA13_HALTER_45': 'num',
               'KBA13_HALTER_50': 'num', 'KBA13_HALTER_55': 'num', 'KBA13_HALTER_60': 'num', 'KBA13_HALTER_65': 'num',
               'KBA13_HALTER_66': 'num', 'KBA13_HERST_ASIEN': 'num', 'KBA13_HERST_AUDI_VW': 'num',
               'KBA13_HERST_BMW_BENZ': 'num', 'KBA13_HERST_EUROPA': 'num', 'KBA13_HERST_FORD_OPEL': 'num',
               'KBA13_HERST_SONST': 'num', 'KBA13_HHZ': 'num', 'KBA13_KMH_0_140': 'num', 'KBA13_KMH_110': 'num',
               'KBA13_KMH_140': 'num', 'KBA13_KMH_140_210': 'num', 'KBA13_KMH_180': 'num', 'KBA13_KMH_210': 'num',
               'KBA13_KMH_211': 'num', 'KBA13_KMH_250': 'num', 'KBA13_KMH_251': 'num', 'KBA13_KRSAQUOT': 'num',
               'KBA13_KRSHERST_AUDI_VW': 'num', 'KBA13_KRSHERST_BMW_BENZ': 'num', 'KBA13_KRSHERST_FORD_OPEL': 'num',
               'KBA13_KRSSEG_KLEIN': 'num', 'KBA13_KRSSEG_OBER': 'num', 'KBA13_KRSSEG_VAN': 'num', 'KBA13_KRSZUL_NEU': 'num',
               'KBA13_KW_0_60': 'num', 'KBA13_KW_110': 'num', 'KBA13_KW_120': 'num', 'KBA13_KW_121': 'num',
               'KBA13_KW_30': 'num', 'KBA13_KW_40': 'num', 'KBA13_KW_50': 'num', 'KBA13_KW_60': 'num',
               'KBA13_KW_61_120': 'num', 'KBA13_KW_70': 'num', 'KBA13_KW_80': 'num', 'KBA13_KW_90': 'num',
               'KBA13_MAZDA': 'num', 'KBA13_MERCEDES': 'num', 'KBA13_MOTOR': 'num', 'KBA13_NISSAN': 'num', 'KBA13_OPEL': 'num',
               'KBA13_PEUGEOT': 'num', 'KBA13_RENAULT': 'num', 'KBA13_SEG_GELAENDEWAGEN': 'num',
               'KBA13_SEG_GROSSRAUMVANS': 'num', 'KBA13_SEG_KLEINST': 'num', 'KBA13_SEG_KLEINWAGEN': 'num',
               'KBA13_SEG_KOMPAKTKLASSE': 'num', 'KBA13_SEG_MINIVANS': 'num', 'KBA13_SEG_MINIWAGEN': 'num',
               'KBA13_SEG_MITTELKLASSE': 'num', 'KBA13_SEG_OBEREMITTELKLASSE': 'num', 'KBA13_SEG_OBERKLASSE': 'num',
               'KBA13_SEG_SONSTIGE': 'num', 'KBA13_SEG_SPORTWAGEN': 'num', 'KBA13_SEG_UTILITIES': 'num',
               'KBA13_SEG_VAN': 'num', 'KBA13_SEG_WOHNMOBILE': 'num', 'KBA13_SITZE_4': 'num', 'KBA13_SITZE_5': 'num',
               'KBA13_SITZE_6': 'num', 'KBA13_TOYOTA': 'num', 'KBA13_VORB_0': 'num', 'KBA13_VORB_1': 'num',
               'KBA13_VORB_1_2': 'num', 'KBA13_VORB_2': 'num', 'KBA13_VORB_3': 'num', 'KBA13_VW': 'num', 'KKK': 'num',
               'KOMBIALTER': 'num', 'KONSUMNAEHE': 'num', 'KONSUMZELLE': 'bin', 'LP_FAMILIE_FEIN': 'cat',
               'LP_FAMILIE_GROB': 'num', 'LP_LEBENSPHASE_FEIN': 'cat', 'LP_LEBENSPHASE_GROB': 'cat', 'LP_STATUS_FEIN': 'num',
               'LP_STATUS_GROB': 'num', 'MIN_GEBAEUDEJAHR': 'num', 'MOBI_RASTER': 'num', 'MOBI_REGIO': 'num',
               'NATIONALITAET_KZ': 'cat', 'ONLINE_AFFINITAET': 'num', 'ORTSGR_KLS9': 'num', 'OST_WEST_KZ': 'cat',
               'PLZ8_ANTG1': 'num', 'PLZ8_ANTG2': 'num', 'PLZ8_ANTG3': 'num', 'PLZ8_ANTG4': 'num', 'PLZ8_BAUMAX': 'cat',
               'PLZ8_GBZ': 'num', 'PLZ8_HHZ': 'num', 'PRAEGENDE_JUGENDJAHRE': 'num', 'REGIOTYP': 'num', 'RELAT_AB': 'num',
               'RETOURTYP_BK_S': 'cat', 'RT_KEIN_ANREIZ': 'num', 'RT_SCHNAEPPCHEN': 'num', 'RT_UEBERGROESSE': 'num',
               'SEMIO_DOM': 'num', 'SEMIO_ERL': 'num', 'SEMIO_FAM': 'num', 'SEMIO_KAEM': 'num', 'SEMIO_KRIT': 'num',
               'SEMIO_KULT': 'num', 'SEMIO_LUST': 'num', 'SEMIO_MAT': 'num', 'SEMIO_PFLICHT': 'num', 'SEMIO_RAT': 'num',
               'SEMIO_REL': 'num', 'SEMIO_SOZ': 'num', 'SEMIO_TRADV': 'num', 'SEMIO_VERT': 'num', 'SHOPPER_TYP': 'cat',
               'SOHO_KZ': 'bin', 'STRUKTURTYP': 'cat', 'UMFELD_ALT': 'num', 'UMFELD_JUNG': 'num', 'UNGLEICHENN_FLAG': 'bin',
               'VERDICHTUNGSRAUM': 'num', 'VERS_TYP': 'cat', 'VHA': 'num', 'VHN': 'num', 'VK_DHT4A': 'num',
               'VK_DISTANZ': 'num', 'VK_ZG11': 'num', 'W_KEIT_KIND_HH': 'num', 'WOHNDAUER_2008': 'num', 'WOHNLAGE': 'cat',
               'ZABEOTYP': 'cat', 'ANREDE_KZ': 'cat', 'ALTERSKATEGORIE_GROB': 'num'}
# Defining funtion to change dtypes according to dtypes_dict:
def change_dtypes(df, dtypes = dtypes_dict):
    '''
    It transforms columns dtypes according to dtypes dictionary.

    Inputs:
    df: original dataframe;
    dtypes: dictionary mapping columns and dtypes.

    Output:
    df: transformed dataframe.
    '''
    # Correcting columns with two types:
    for col in list(dtypes.keys()):
        if dtypes[col] == 'cat':
            df[col] = df[col].astype('category')
        else:
            df[col] = pd.to_numeric(df[col], errors = 'coerce')

    return df

# Defining function to engineer new features:
def feature_engineer(df):
    '''
    It uses some original features to create new and more informative ones.
    * CAMEO_INTL_2015 splits into CAMEO_INTL_FAM_STATUS and CAMEO_INTL_FAM_COMPOSITION.
    * PRAEGENDE_JUGENDJAHRE splits into YOUTH_DECADE and AVANT_GARDE.
    * ALTER_HH is simplified representing decades.

    Input:
    df: original dataframe.

    Output:
    df: transformed dataframe.
    '''
    # Target columns to be transformed:
    feat1 = 'CAMEO_INTL_2015'
    feat2 = 'PRAEGENDE_JUGENDJAHRE'
    feat3 = 'ALTER_HH'

    # Creating CAMEO_INTL_FAM_STATUS feature:
    df['CAMEO_INTL_FAM_STATUS'] = [int(str(df[feat1].iloc[i])[0]) if str(df[feat1].iloc[i]) != 'nan' \
                                   else np.nan for i in range(df.shape[0])]

    # Creating CAMEO_INTL_FAM_COMPOSITION feature:
    df['CAMEO_INTL_FAM_COMPOSITION'] = [int(str(df[feat1].iloc[i])[1]) if str(df[feat1].iloc[i]) != 'nan' \
                                        else np.nan for i in range(df.shape[0])]

    # Creating YOUTH_DECADE feature:
    df['YOUTH_DECADE'] = [4 if df[feat2].iloc[i] in [1, 2] \
                          else 5 if df[feat2].iloc[i] in [3, 4] \
                          else 6 if df[feat2].iloc[i] in [5, 6, 7] \
                          else 7 if df[feat2].iloc[i] in [8, 9] \
                          else 8 if df[feat2].iloc[i] in [10, 11, 12, 13] \
                          else 9 if df[feat2].iloc[i] in [14, 15] \
                          else np.nan for i in range(df.shape[0])]

    # Creating AVANT_GARDE feature:
    df['AVANT_GARDE'] = [0 if df[feat2].iloc[i] in [1, 3, 5, 8, 10, 12, 14] \
                         else 1 if df[feat2].iloc[i] in [2, 4, 6, 7, 9, 11, 13, 15] \
                         else np.nan for i in range(df.shape[0])]

    # Deleting original columns:
    df.drop(columns = [feat1, feat2], inplace = True)

    # Simplifying ALTER_HH to represent decades:
    df[feat3] = [1 if df[feat3].iloc[i] in [1, 2, 3] \
                 else 2 if df[feat3].iloc[i] in [4, 5] \
                 else 3 if df[feat3].iloc[i] in [6, 7] \
                 else 4 if df[feat3].iloc[i] in [8, 9] \
                 else 5 if df[feat3].iloc[i] in [10, 11] \
                 else 6 if df[feat3].iloc[i] in [12, 13] \
                 else 7 if df[feat3].iloc[i] in [14, 15] \
                 else 8 if df[feat3].iloc[i] in [16, 17] \
                 else 9 if df[feat3].iloc[i] in [18, 19] \
                 else np.nan for i in range(df.shape[0])]

    return df

# Defining dtypes for new features:
new_feat_dtypes_dict = {'AVANT_GARDE': 'cat',
                        'CAMEO_DEU_REPRESENTATION': 'num',
                        'CAMEO_INTL_FAM_COMPOSITION': 'num',
                        'CAMEO_INTL_FAM_STATUS': 'num',
                        'YOUTH_DECADE': 'num'}

# Creating dictionary to map each feature to its correspondent information level:
info_level = {'person': ['ANREDE_KZ', 'ALTERSKATEGORIE_GROB', 'AVANT_GARDE', 'CJT_GESAMTTYP', 'CJT_KATALOGNUTZER', 'CJT_TYP_6',
                         'FINANZ_ANLEGER', 'FINANZ_HAUSBAUER', 'FINANZTYP', 'GFK_URLAUBERTYP', 'HEALTH_TYP', 'LP_FAMILIE_FEIN',
                         'LP_FAMILIE_GROB', 'LP_LEBENSPHASE_FEIN', 'LP_LEBENSPHASE_GROB', 'LP_STATUS_GROB', 'NATIONALITAET_KZ',
                         'OST_WEST_KZ', 'RETOURTYP_BK_S', 'SEMIO_ERL', 'SEMIO_FAM', 'SEMIO_KRIT', 'SEMIO_KULT', 'SOHO_KZ',
                         'SEMIO_LUST', 'SEMIO_MAT', 'SEMIO_RAT', 'SEMIO_REL', 'SEMIO_SOZ', 'SEMIO_TRADV', 'SEMIO_VERT',
                         'SHOPPER_TYP', 'VERS_TYP', 'YOUTH_DECADE', 'ZABEOTYP'],
              'household': ['AKT_DAT_KL', 'ANZ_KINDER', 'ANZ_STATISTISCHE_HAUSHALTE', 'ANZ_TITEL', 'CAMEO_DEU_REPRESENTATION',
                            'CAMEO_INTL_FAM_COMPOSITION', 'CAMEO_INTL_FAM_STATUS', 'D19_LETZTER_KAUF_BRANCHE',
                            'HH_EINKOMMEN_SCORE', 'WOHNDAUER_2008', 'W_KEIT_KIND_HH', 'RT_KEIN_ANREIZ', 'RT_SCHNAEPPCHEN',
                            'RT_UEBERGROESSE'],
              'microcell': ['ANZ_HH_TITEL', 'DSL_FLAG', 'HH_DELTA_FLAG', 'KBA05_ALTER1', 'KBA05_ALTER2', 'KBA05_ALTER3',
                            'KBA05_ALTER4', 'KBA05_ANHANG', 'KBA05_ANTG2', 'KBA05_ANTG3', 'KBA05_ANTG4', 'KBA05_CCM1',
                            'KBA05_CCM2', 'KBA05_CCM3', 'KBA05_CCM4', 'KBA05_DIESEL', 'KBA05_FRAU', 'KBA05_HERST4',
                            'KBA05_HERST5', 'KBA05_HERSTTEMP', 'KBA05_KRSAQUOT', 'KBA05_KRSHERST1', 'KBA05_KRSHERST2',
                            'KBA05_KRSHERST3', 'KBA05_KW2', 'KBA05_KW3', 'KBA05_MAXAH', 'KBA05_MAXBJ', 'KBA05_MAXHERST',
                            'KBA05_MAXSEG', 'KBA05_MAXVORB', 'KBA05_MOD1', 'KBA05_MOD2', 'KBA05_MOD3', 'KBA05_MOD4',
                            'KBA05_MODTEMP', 'KBA05_MOTOR', 'KBA05_MOTRAD', 'KBA05_SEG1', 'KBA05_SEG10', 'KBA05_SEG2',
                            'KBA05_SEG3', 'KBA05_SEG4', 'KBA05_SEG5', 'KBA05_SEG6', 'KBA05_SEG7', 'KBA05_SEG8', 'KBA05_SEG9',
                            'KBA05_VORB0', 'KBA05_VORB1', 'KBA05_VORB2', 'KBA05_ZUL1', 'KBA05_ZUL2', 'KBA05_ZUL3',
                            'KBA05_ZUL4', 'KONSUMZELLE', 'MIN_GEBAEUDEJAHR', 'STRUKTURTYP', 'UMFELD_ALT', 'UMFELD_JUNG',
                            'WOHNLAGE'],
              'macrocell': ['BALLRAUM', 'GEBAEUDETYP_RASTER', 'GEBAEUDETYP', 'GEMEINDETYP', 'INNENSTADT', 'KBA13_AUDI',
                            'KBA13_AUTOQUOTE', 'KBA13_BJ_2000', 'KBA13_BJ_2006', 'KBA13_BJ_2008', 'KBA13_BJ_2009', 'KBA13_BMW',
                            'KBA13_CCM_0_1400', 'KBA13_CCM_1000', 'KBA13_CCM_1200', 'KBA13_CCM_1400', 'KBA13_CCM_1401_2500',
                            'KBA13_CCM_1500', 'KBA13_CCM_1600', 'KBA13_CCM_1800', 'KBA13_CCM_2000', 'KBA13_CCM_2500',
                            'KBA13_CCM_2501', 'KBA13_CCM_3000', 'KBA13_CCM_3001', 'KBA13_FAB_ASIEN', 'KBA13_FIAT',
                            'KBA13_FORD', 'KBA13_HALTER_20', 'KBA13_HALTER_25', 'KBA13_HALTER_35', 'KBA13_HALTER_40',
                            'KBA13_HALTER_45', 'KBA13_HALTER_50', 'KBA13_HALTER_55', 'KBA13_HALTER_60', 'KBA13_HALTER_65',
                            'KBA13_HALTER_66', 'KBA13_HERST_ASIEN', 'KBA13_HERST_EUROPA', 'KBA13_HERST_SONST', 'KBA13_KMH_140',
                            'KBA13_KMH_180', 'KBA13_KMH_210', 'KBA13_KMH_250', 'KBA13_KMH_251', 'KBA13_KRSAQUOT',
                            'KBA13_KRSHERST_AUDI_VW', 'KBA13_KRSHERST_BMW_BENZ', 'KBA13_KRSHERST_FORD_OPEL',
                            'KBA13_KRSSEG_KLEIN', 'KBA13_KRSSEG_OBER', 'KBA13_KRSZUL_NEU', 'KBA13_KW_110', 'KBA13_KW_120',
                            'KBA13_KW_121', 'KBA13_KW_30', 'KBA13_KW_40', 'KBA13_KW_50', 'KBA13_KW_60', 'KBA13_KW_61_120',
                            'KBA13_KW_70', 'KBA13_KW_80', 'KBA13_KW_90', 'KBA13_MAZDA', 'KBA13_MERCEDES', 'KBA13_MOTOR',
                            'KBA13_NISSAN', 'KBA13_OPEL', 'KBA13_PEUGEOT', 'KBA13_RENAULT', 'KBA13_SEG_GELAENDEWAGEN',
                            'KBA13_SEG_KLEINWAGEN', 'KBA13_SEG_KOMPAKTKLASSE', 'KBA13_SEG_MINIWAGEN', 'KBA13_SEG_MITTELKLASSE',
                            'KBA13_SEG_OBEREMITTELKLASSE', 'KBA13_SEG_OBERKLASSE', 'KBA13_SEG_SONSTIGE',
                            'KBA13_SEG_SPORTWAGEN', 'KBA13_SEG_UTILITIES', 'KBA13_SEG_VAN', 'KBA13_SEG_WOHNMOBILE',
                            'KBA13_SITZE_5', 'KBA13_SITZE_6', 'KBA13_TOYOTA', 'KBA13_VORB_0', 'KBA13_VORB_1', 'KBA13_VORB_1_2',
                            'KBA13_VORB_2', 'KBA13_VORB_3', 'KBA13_VW', 'MOBI_REGIO', 'PLZ8_ANTG2', 'PLZ8_ANTG4',
                            'PLZ8_BAUMAX', 'PLZ8_GBZ', 'PLZ8_HHZ', 'VK_ZG11', 'VK_DHT4A', 'VHN', 'VHA', 'VERDICHTUNGSRAUM',
                            'UNGLEICHENN_FLAG'],
              'community': ['ARBEIT', 'ORTSGR_KLS9', 'RELAT_AB']}

# Defining CAMEO_DEU_2015 transformation:
def transform_cameo_deu(df):
    '''
    It simplifies CAMEO_DEU_2015 classes according to the representation pattern presented in the comparison
    between customers and the general population.
    '''
    # Creating new column:
    feat = 'CAMEO_DEU_2015'
    df['CAMEO_DEU_REPRESENTATION'] = [0 if df[feat].iloc[i] in ['6A', '7A', '7B', '7C', '8A', '8B', '8C', '8D', '9A', '9B',
                                                                '9C', '9D'] \
                                      else 1 if df[feat].iloc[i] in ['5A', '5B', '5C', '6B', '7D'] \
                                      else 2 if df[feat].iloc[i] in ['3A', '3B', '3C', '4B', '4C', '4E', '5E', '5F', '6C',
                                                                     '6D', '6E', '6F', '7E', '9E'] \
                                      else 3 if df[feat].iloc[i] in ['1A', '1B', '1C', '1D', '2A', '2B', '2C', '2D', '3D',
                                                                     '4A', '5D'] \
                                      else np.nan for i in range(df.shape[0])]

    # Transforming the column to categorical type:
    df['CAMEO_DEU_REPRESENTATION'] = df['CAMEO_DEU_REPRESENTATION'].astype('category')

    # Deliting original column:
    df.drop(columns = [feat], inplace = True)

    return df
