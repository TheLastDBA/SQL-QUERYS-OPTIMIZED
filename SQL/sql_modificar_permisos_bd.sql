-- Denegar SELECT en todas las tablas del esquema esw_prod
DECLARE @sql NVARCHAR(MAX) = N'';

SELECT @sql = @sql + '
DENY SELECT ON ' + QUOTENAME(s.name) + '.' + QUOTENAME(t.name) + ' TO user_etl;'
FROM sys.tables t
INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
WHERE s.schema_id = '1';

PRINT @sql; -- Revisa antes de ejecutar
EXEC sp_executesql @sql;

-- Conceder SELECT sobre las tablas específicas usadas en la consulta
GRANT SELECT ON esw_prod.dbo.esw_ordenes_produccion TO user_etl;
GRANT SELECT ON esw_prod.dbo.esw_items_ordenes TO user_etl;
GRANT SELECT ON esw_prod.dbo.esw_sistemas_linea TO user_etl;
GRANT SELECT ON esw_prod.dbo.esw_estado_sistema TO user_etl;
GRANT SELECT ON esw_prod.dbo.esw_lineas TO user_etl;
