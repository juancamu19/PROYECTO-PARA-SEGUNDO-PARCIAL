import pandas as pd

'''Se crea la clase Empresa'''
class Empresa():
    
    '''Funcion para consultar las ventas por mes'''
    def gestionVentasxmes(mes):
        nombresColumnas = ['idAlq', 'idRes', 'dni', 'patente', 'fecInicio', 'fecFin','fechadev','monto']
        df = pd.read_csv('Alquileres.csv', names = nombresColumnas)
        df[['dia', 'mes', 'anio']] = df['fecInicio'].str.split('-',expand=True)
        df_filtrado = df.loc[df['mes'] == mes]
        sumaTotal = df_filtrado['monto'].sum()
        print(df_filtrado)
        print(' Y La suma total de alquileres para este mes es ', sumaTotal)
        return sumaTotal
    
    '''Funcion para consultar las ventas por día'''
    def gestionVentasxdia(dia):
        nombresColumnas = ['idAlq', 'idRes', 'dni', 'patente', 'fecInicio', 'fecFin','fechadev','monto']
        df = pd.read_csv('Alquileres.csv', names=nombresColumnas)
        filtro = (df['fecInicio'] == dia)
        df_filtrado = df[filtro]
        sumaTotal = df_filtrado['monto'].sum()
        print(df_filtrado)
        print(' Y La suma total de alquileres para este dia es ', sumaTotal)
        return sumaTotal



if __name__=='__main__':
    pass
