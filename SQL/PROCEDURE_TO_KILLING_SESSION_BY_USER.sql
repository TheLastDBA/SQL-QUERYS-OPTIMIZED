
--SELECT distinct
--    t.object_id as objectId,
--    p.rows AS tableRowCount
--FROM 
--    sys.tables t
--INNER JOIN      
--    sys.indexes i ON t.OBJECT_ID = i.object_id
--INNER JOIN 
--    sys.partitions p ON i.object_id = p.OBJECT_ID AND i.index_id = p.index_id
--INNER JOIN
--    sys.schemas s ON t.schema_id = s.schema_id
--WHERE 
--    t.NAME NOT LIKE 'dt%' 
--    AND t.is_ms_shipped = 0
--    AND i.OBJECT_ID > 255 
--    AND s.name  is not null 


--	kill 381

--	select * from sys.dm_exec_requests where blocking_session_id != 0
--	SELECT * FROM sys.sysprocesses where blocked !=  0

--	execute sp_who 455


-- select user_name();


BEGIN; 

/** BLOQUE ANÓNIMO CREADO POR  $$$ DIDIER ACUÑA $$$, ESTE BLOQUE ES CAPAZ DE HACER KILL A TODAS LAS SESIONES DE UN USUARIO,
CLARAMENTE DEBES USARLO SOLO PARA SACAR AL USUARIO QUE MÁS SESIONES BLOQUEA
Y DICHO USUARIO SERÁ INTERRUMPIDO. 

CLARAMENTE PUEDO HACER UN PROCEDURE QUE TERMINE CONEXIONES DE UNA FORMA MÁS ARMÓNICA Y ESPECÍFICA
(COMO POR EJEMPLO: SACAR TODAS LAS CONEXIONES CON ESTADO DE BLOQUEO DADO UNA MEDIA DE BLOQUEO DE CONEXIONES BY SESSION)
PERO PARA EFECTOS RÁPIDOS Y CONFIANDO EN QUE ERES UN BUEN DBA (AQUEL QUE SABE QUE TERMINAR Y QUE NO) SE HIZO ASI DE SIMPLE.
**/

begin try
-- inicio try


DECLARE @STATEMENT AS NVARCHAR(MAX) = '';
DECLARE @LOGIN AS NVARCHAR(300) = ''; -- ESCRIBE EL USUARIO OBJETIVO
DECLARE @EXECUTOR AS NVARCHAR(300) = ''; -- SI DESEAS EJECUTAR LA SETENCIA CON OTRA SESSION DIFERENTE A TU ACTUAL

Print 'Su session actual es: '+ current_user +' con user name de: '+ user_name();

IF @EXECUTOR != '' -- SI QUIERES PUEDES ADAPTARLO A VALIDAR USUARIOS EXISTENTE ES SYS logins
BEGIN
EXECUTE AS LOGIN = @EXECUTOR ; -- 'Your preferred login session';
END
else
print 'Ejecutor personalizado no asignado. ignorar...'



if exists (select *  from sys.sysprocesses where loginame =   @LOGIN)
begin -- inicio if

PRINT 'Login valido para manejar ';

print ' Killing with user: '+SUSER_NAME()+' '+USER_NAME();
SET @STATEMENT = (
SELECT  STRING_AGG(concat('kill ', session_id,' ;'),' ')-- , login_name, host_name, program_name, status
FROM sys.dm_exec_sessions
WHERE login_name = @LOGIN);

PRINT @STATEMENT;


EXECUTE sp_executesql @STATEMENT;


end -- fin if
else
PRINT 'Tu login no tiene sessiones en el server.';


--final try
end try
begin catch
PRINT 'ERROR HANLING: ';
THROW 

end catch;



END; 



