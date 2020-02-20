import pandas as pd
from chembl_webresource_client.new_client import new_client


if __name__ =='__main__':
    #Working directory
    wd="C://Users/Kevin/Desktop/Chembl/"
    #Read input
    data=pd.read_table(wd+'Proteomics_results.txt',header=0)
    data=data.dropna()
    #Specify column name for Gene Symbols
    proteins=list(data['Gene Symbol'])
    data.index=data['Gene Symbol']
    #print(proteins)
    Mapped={}
    for protein in proteins:
        records=new_client.target.filter(target_components__target_component_synonyms__component_synonym=protein)
        #print([(x['target_chembl_id'],x['pref_name']) for x in records])
        chembl_id=[(x['target_chembl_id']) for x in records]
        try:
            chembl_id=chembl_id[0]
            activities=new_client.mechanism.filter(target_chembl_id=chembl_id)
            compounds=[x['molecule_chembl_id'] for x in activities]
            compound_list=list()
            for compound in compounds:
                mol=new_client.molecule.get(compound)
                compound_list.append(mol['pref_name'])
            Mapped[protein]=list(compound_list)
        except IndexError:
            pass
    #print(Mapped)
    #Specify name for output
    df=open(wd+'output_mapped.txt',"w+")
    for key in Mapped.keys():
        for comp in Mapped[key]:
            df.write(key + '\t' +str(data.loc[key,'Accession']) +'\t'+comp +'\t'+'compound'+'\n')
    df.close()



