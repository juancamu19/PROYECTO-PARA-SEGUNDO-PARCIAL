import pandas as pd

'''Se crea la clase Empresa. Notar que, a priori, al no tener más de una sede, no vale la pena colocar un método
constructor en esta clase. La empresa se considera como única, y en ella se guardan los métodos de gestión, haciendo
uso de la base de datos para alquiler, que es quien almacena la contabilidad en el contexto de nuestro proyecto.

Para ambos métodos se trabajo con el dataframe de pandas, esto facilita el trabajo con tablas y filtrado de las mismas.'''
class Empresa():
    
    '''Funcion para consultar las ventas por mes. Un empleado puede filtrar la informacion de alquileres por mes, 
    y asi evaluar informes, tendencias, etc.'''
    
    def gestionVentasxmes(mes):
        """_summary_

        Args:
            mes (_type_): _description_

        Returns:
            _type_: _description_
        """
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
        """_summary_

        Args:
            dia (_type_): _description_

        Returns:
            _type_: _description_
        """
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
