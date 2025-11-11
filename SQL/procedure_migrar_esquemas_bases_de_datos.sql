

  
DECLARE @SQLs NVARCHAR(MAX); 
SET @SQLs = '  USE TGQ;
execute  TGQ.dbo.[migrar_base_de_datos_by_ddr_format] ''TGQ''; ';


EXECUTE sp_executesql @SQLs;



USE [TGQ]
GO
CREATE SCHEMA [tgq] AUTHORIZATION [dbo]
GO


USE [TGQ]
GO
/****** Object:  StoredProcedure [dbo].[migrar_base_de_datos_by_ddr_format]    Script Date: 11/11/2025 11:48:23 a. m. ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO

ALTER PROCEDURE [dbo].[migrar_base_de_datos_by_ddr_format] @VALIDAR_EXISTENCIA_BD VARCHAR(30) As 

DECLARE @COUNT INT = 0;
DECLARE @ERRORS NVARCHAR(MAX);
DECLARE @MULTIPLICADOR INT = 0;
DECLARE @SQL NVARCHAR(MAX);
DECLARE @ITERA INT = 0;
DECLARE @MENSAJE NVARCHAR(10) = '';
DECLARE @ESQUEMA NVARCHAR(30) = '';



BEGIN
begin try

-- Validacion de base de datos, obviamente puede validar mas cosas y hacer este procedure mucho mas dinamico pero para efecto puntual, decido solo validar si existe la bd DESTINO

IF EXISTS (select * from sys.databases where name = @VALIDAR_EXISTENCIA_BD) BEGIN
PRINT 'Existencia valida.'; 

EXECUTE AS LOGIN = 'didier.acuna';
--SET @ESQUEMA = 'USE [TGQ]
--GO
--CREATE SCHEMA [tgq] AUTHORIZATION [db_owner]
--GO
--';   

EXECUTE sp_executesql @ESQUEMA;

END ELSE 
BEGIN
print 'Ingresa una base de datos valida, saliendo...'; 
return;
END;




PRINT 'CREANDO TABLA PARA GUARDAR DDLs';
CREATE TABLE #executables (id int identity primary key, exec_sql Nvarchar(max)); 

PRINT 'INSERTANDO TODOS LOS DDLs EN TABLA EJECUTABLE';
INSERT INTO #executables(exec_sql)
select 
  CONCAT(
    'ALTER SCHEMA tgq transfer tgp.[', 
    name, '];'
  ) as exec_sql 
from 
  TGQ.sys.tables 
where 
  schema_id =(
    select 
      schema_id 
    from 
      TGQ.sys.schemas 
    where 
      name = 'tgp'
  ) 
UNION ALL 
  -- ALTER SCHEMA EsquemaNuevo TRANSFER EsquemaActual.NombreTabla
SELECT 
  CONCAT(
    'ALTER SCHEMA tgq transfer tgp.[', 
    name, '];'
  ) as exec_sql 
FROM 
  TGQ.sys.procedures 
WHERE 
  schema_id = SCHEMA_ID('tgp') 
UNION ALL 
  -- Actualiza funciones
SELECT 
  CONCAT(
    'ALTER SCHEMA tgq transfer tgp.[', 
    name, '];'
  ) as exec_sql 
FROM 
  TGQ.sys.objects 
WHERE 
  schema_id = SCHEMA_ID('tgp') 
  AND type IN ('FN', 'IF', 'TF', 'FS', 'FT') 
UNION ALL 
select 
  CONCAT(
    'ALTER SCHEMA tgq transfer tgp.[', 
    name, '];'
  ) as exec_sql 
from 
  TGQ.sys.views 
where 
  schema_id = SCHEMA_ID('tgp');



PRINT 'INSTANCIANDO VARIABLES POST WHILE';
SET 
  @COUNT = 0;
SET 
  @MULTIPLICADOR = 1000;
set 
  @ITERA = 0;
SET 
  @MENSAJE = '';

PRINT 'PRIMERA EJECUCION DE DDLs';

SET 
  @SQL = (
     SELECT STRING_AGG(exec_sql, ' ')
                FROM (
                    SELECT exec_sql
                    FROM #executables
                    WHERE id > @ITERA AND id <= @ITERA + @MULTIPLICADOR
                   -- ORDER BY id
                ) AS sub
  );
EXECUTE sp_executesql @SQL;


PRINT 'ENTRANDO AL WHILE';


WHILE @COUNT IS NOT NULL BEGIN 
SET 
  @ITERA = @ITERA + 1000;
SET 
  @SQL = (
     SELECT STRING_AGG(exec_sql, ' ')
                FROM (
                    SELECT exec_sql
                    FROM #executables
                    WHERE id > @ITERA AND id <= @ITERA + @MULTIPLICADOR
                    -- ORDER BY id
                ) as sub ); 

    SET 
      @MENSAJE = @ITERA;


PRINT ' CANTIDAD DE TABLAS MIGRADAS: ' + @MENSAJE;

EXECUTE sp_executesql @SQL;


IF @SQL IS NULL BEGIN 
SET 
  @COUNT = NULL;
PRINT 'FIN DE WHILE';
END;



END;



PRINT 'ESQUEMAS MIGRADOS CON EXITO';
PRINT 'BORRANDO TEMPORALES';
DROP 
  TABLE #executables; 
  end try begin catch 
SET 
  @ERRORS = (
    SELECT 
      CONCAT(
        ERROR_NUMBER(), 
        ' AS NumeroError |', 
        ERROR_MESSAGE(), 
        'AS MensajeError |', 
        ERROR_SEVERITY(), 
        'AS Severidad |', 
        ERROR_STATE(), 
        'AS Estado |', 
        ERROR_LINE(), 
        'AS Linea |', 
        ERROR_PROCEDURE(), 
        'AS Procedimiento | Error time: ', 
        CURRENT_TIMESTAMP
      )
  );
INSERT INTO [master].[dbo].[log_migracionesTGP](evento) 
values 
  (@ERRORS);
PRINT @ERRORS;
THROW;
END CATCH;
END;
