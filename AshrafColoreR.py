def AshrafColoreR():
    import pandas as pd
    filename= ('phylum.table')
    df_Phylum = pd.read_table(filename,names='A')
    with open('Phylum_Color.r','w') as hndl:
    #     i=0
        hndl.write('colors=colorRampPalette(c(')
    #     hndl.write('colors')
        for i in df_Phylum.index:
            hndl.write(df_Phylum.loc[:,'A'][i].split(' ')[0]+'('+df_Phylum.loc[:,'A'][i].split(' ')[1]+'),')
    #     hndl.write('))')
    with open('Phylum_Color.r','r') as hndl:
        data = hndl.readlines()
    data = str(data)
    data = data[2:-4]
    with open('Phylum_Color.r','w') as hndl:
        hndl.write(data+')))')
AshrafColoreR()
