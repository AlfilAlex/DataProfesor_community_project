import pandas as pd
import numpy as np


def basic_filtering(df):

    target_pref_name = (df['Target_Name'] == 'Beta-lactamase AmpC')
    bao_label = df['BAO_Label'] == 'assay format'
    standard_relation = df['Standard_Relation'] == "'='"
    standard_type = (df['Standard_Type'] == 'IC50') | (
        df['Standard_Type'] == 'Potency') | (df['Standard_Type'] == 'Ki')

    # df_filtered = df[standard_relation &
    df_filtered = df[target_pref_name & bao_label & standard_relation &
                     standard_type][['Smiles', 'Standard_Value', 'pChEMBL_Value']]

    # Procedemos ahora a eliminar files con valores perdidos
    smiles_not_null = df_filtered['Smiles'].notnull()
    smiles_not_empty = df_filtered['Smiles'] != ''

    pchembl_value_not_nut = df_filtered['pChEMBL_Value'].notnull()
    pchembl_value_not_empty = df_filtered['pChEMBL_Value'] != ''

    df_without_missing = df_filtered[smiles_not_null &
                                     smiles_not_empty & pchembl_value_not_nut & pchembl_value_not_empty]
    print(len(df_without_missing))
    return df_without_missing


def smiles_standarization(df):
    from rdkit.Chem.MolStandardize import rdMolStandardize

    def cleaning(df_row):
        smile = df_row[0]
        stadarized_smiles = None
        try:
            stadarized_smiles = rdMolStandardize.StandardizeSmiles(smile)
        except:
            print(f'The molecule {smile} is not stadarizable')

        return stadarized_smiles

    df['Smiles'] = df.apply(cleaning, axis='columns').dropna()

    return df


def duplicate_mean_aggregation(df):

    df = df[['Smiles', 'pChEMBL_Value']]
    df = df.groupby('Smiles', as_index=False).mean()

    print(len(df))
    return df


def main_filtering(df, name):
    print('= = = = = = = = = = = = = = = =')
    print(
        f'There are {len(df)} molecules in the {name} dataset before filtering')
    df_bf = basic_filtering(df)
    # df_st = smiles_standarization(df_bf)
    # df_final = duplicate_mean_aggregation(df_st)

    print(
        f'There are {len(df_bf)} molecules in the {name} dataset after filtering')

    return df_bf


def standarization_and_aggregation(df, name):
    print('= = = = = = = = = = = = = = = =')
    print(
        f'There are {len(df)} molecules in the {name} dataset before standarization_and_aggregation')
    df_st = smiles_standarization(df)
    df_final = duplicate_mean_aggregation(df_st)

    print(
        f'There are {len(df_final)} molecules in the {name} dataset after standarization_and_aggregation')

    return df_final
