import pandas as pd
import numpy as np
#Read Files
data20=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2020.csv',delimiter=';')
data19=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2019.csv',delimiter=';')
data18=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2018.csv',delimiter=';')
data17=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2017.csv',delimiter=';')
data16=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2016.csv',delimiter=';')
data15=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2015.csv',delimiter=';')
data14=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2014.csv',delimiter=';')
data13=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2013.csv',delimiter=';')
data12=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2012.csv',delimiter=';')
data11=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2011.csv',delimiter=';')
data10=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2010.csv',delimiter=';')
data09=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2009.csv',delimiter=';')
data08=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2008.csv',delimiter=';')
data07=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2007.csv',delimiter=';')
data06=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2006.csv',delimiter=';')
data05=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2005.csv',delimiter=';')
data04=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2004.csv',delimiter=';')
data03=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2003.csv',delimiter=';')
data02=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2002.csv',delimiter=';')
data01=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/data2001.csv',delimiter=';')
edias=['D01','D02','D03','D04','D05','D06','D07','D08','D09','D10','D11','D12','D13','D14','D15','D16','D17','D18','D19','D20','D21','D22','D23','D24','D25','D26','D27','D28','D29','D30','D31']
#
codigos=pd.read_csv('/home/sauronrr/git/practicasPython/pollutionMadrid/codigos.csv',delimiter=';')

#Join data 
frames=[data01, data02, data03, data04, data05, data06, data07, data08, data09, data10,
       data11,data12,data13,data14,data15,data16,data17,data18,data19,data20]
full_data=pd.concat(frames)
def getDescMagnitud(imagnitud):
    x=codigos[codigos['Cod']==imagnitud]
    return x.iloc[0,1]
def getDescUnidad(imagnitud):
    x=codigos[codigos['Cod']==imagnitud]
    return x.iloc[0,3]
    
def getDfMagnitud (DF,imagnitud):
    return DF[DF['MAGNITUD']==imagnitud]

def getDfPuntoMuestreo (DF,punto):
    return DF[DF['PUNTO_MUESTREO']==punto]
    
def printPuntosMuestreo  (DF):
    return DF['PUNTO_MUESTREO'].unique()

def printMagnitud  (DF):
    return DF['MAGNITUD'].unique()
    
def valoresMax(DF):
    iano=[]
    imes=[]
    imaxa=[]
    imaxm=[]
    ipunto=[]
    for punto in DF['PUNTO_MUESTREO'].unique():
        #print(f'{punto}:')
        for vano  in DF[DF['PUNTO_MUESTREO']==punto]['ANO'].unique():
            
            vfiltroAno=DF[DF.ANO==int(vano)]
            if vfiltroAno.empty:
                pass
                #print('Sin datos')
            else:
                maxdia=vfiltroAno[edias].max()
                maxano=maxdia.max()
                #print(f'\t{vano}: max: {maxano}')
                for  mes in np.sort(vfiltroAno['MES'].unique()):
                    vfiltroMes=vfiltroAno[vfiltroAno.MES==int(mes)]
                    if vfiltroMes.empty:
                        pass
                    #    print('Sin datos')
                    else:
                        maxdia=vfiltroMes[edias].max()
                        maxmes=maxdia.max()
                        iano.append(vano)
                        imes.append(mes)
                        imaxa.append(maxano)
                        imaxm.append(maxmes)
                        ipunto.append(punto)
                        
                        #print(f'\t\t{mes}: max: {maxmes}')
                        
    l={'punto':ipunto,'ano':iano,'mes':imes,'valano':imaxa,'valmes':imaxm}
    return pd.DataFrame(l,columns=['punto','ano','mes','valano','valmes'])            

def valoresMin(DF):
    iano=[]
    ipunto=[]
    imes=[]
    imina=[]
    iminm=[]
    for punto in DF['PUNTO_MUESTREO'].unique():
        #print(f'{punto}:')
        for vano  in DF[DF['PUNTO_MUESTREO']==punto]['ANO'].unique():
            
            vfiltroAno=DF[DF.ANO==int(vano)]
        if vfiltroAno.empty:
                pass
                #print('Sin datos')
        else:
                positivos=vfiltroAno[edias]>0
                a=vfiltroAno[edias]
                mindia=a[positivos].min()
                minano=mindia.min()
                #print(f'\t{vano}: min: {minano}')
                for  mes in np.sort(vfiltroAno['MES'].unique()):
                    vfiltroMes=vfiltroAno[vfiltroAno.MES==int(mes)]
                    positivos=vfiltroMes[edias]>0
                    a=vfiltroMes[positivos]
                    if a.empty:
                        pass
                    #    print('Sin datos')
                    else:
                        mindia=a[edias].min()
                        minmes=mindia.min()
                        iano.append(vano)
                        imes.append(mes)
                        imina.append(minano)
                        iminm.append(minmes)
                        ipunto.append(punto)
                        
                        #print(f'\t\t{mes}: max: {minmes}')
                        
    l={'punto':ipunto,'ano':iano,'mes':imes,'valano':imina,'valmes':iminm}
    return pd.DataFrame(l,columns=['punto','ano','mes','valano','valmes'])

def valoresMean(DF):
    iano=[]
    ipunto=[]
    imes=[]
    imina=[]
    iminm=[]
    for punto in DF['PUNTO_MUESTREO'].unique():
        #print(f'{punto}:')
        for vano  in DF[DF['PUNTO_MUESTREO']==punto]['ANO'].unique():
            
            vfiltroAno=DF[DF.ANO==int(vano)]
        if vfiltroAno.empty:
                pass
                #print('Sin datos')
        else:
                positivos=vfiltroAno[edias]>0
                a=vfiltroAno[edias]
                mindia=a[positivos].mean()
                minano=mindia.mean()
                #print(f'\t{vano}: min: {minano}')
                for  mes in np.sort(vfiltroAno['MES'].unique()):
                    vfiltroMes=vfiltroAno[vfiltroAno.MES==int(mes)]
                    positivos=vfiltroMes[edias]>0
                    a=vfiltroMes[positivos]
                    if a.empty:
                        pass
                    #    print('Sin datos')
                    else:
                        mindia=a[edias].mean()
                        minmes=mindia.mean()
                        iano.append(vano)
                        imes.append(mes)
                        imina.append(minano)
                        iminm.append(minmes)
                        ipunto.append(punto)
                        
                        #print(f'\t\t{mes}: max: {minmes}')
                        
    l={'punto':ipunto,'ano':iano,'mes':imes,'valano':imina,'valmes':iminm}
    return pd.DataFrame(l,columns=['punto','ano','mes','valano','valmes'])

#se debe pasar un dataFrame con los valores de una unica magnitud y un unico punto de muestreo
def plotPoluAnual(DF):
    imagnitud=DF['MAGNITUD'].iloc[0]
    df=getDfMagnitud(DF,imagnitud)
    puntomuestreo=DF['PUNTO_MUESTREO'].iloc[0]
    if df.empty:
        print(f'La muestra {imagnitud} no tiene datos')
    else:
        x=codigos[codigos['Cod']==imagnitud]
        ltittle=x.iloc[0,1]
        ylabel=x.iloc[0,3]
        df2=valoresMax(df)
        df1=df2.groupby('ano')['valano'].unique()
        y=[float(i) for i in df1]
        x=[v for v in df1.index]
        c=[x,y]
        l={'ejex':x,'ejey':y}
        pl=pd.DataFrame(l,columns=['ejex','ejey']) 
        
        ax=pl.plot.bar(figsize=(10,10),x='ejex',y='ejey',label='ano')
        ax.set_ylabel(ylabel)
        ax.set_title('Concentracion de '+ltittle+' en la estacion '+str(puntomuestreo))
