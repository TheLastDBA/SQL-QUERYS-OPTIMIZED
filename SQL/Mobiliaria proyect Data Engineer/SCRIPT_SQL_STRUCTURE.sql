
CREATE DATABASE [Mobiliaria_carpintero_wh]
GO

  USE [Mobiliaria_carpintero_wh]
GO

  CREATE SCHEMA bronze
  go

  CREATE SCHEMA silver
  go

  CREATE SCHEMA gold;

  go




/****** Object:  Table [bronze].[base_dato_entrada_dwh]    Script Date: 16/01/2026 11:31:00 a. m. ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO





-- STAGE TABLES 
CREATE TABLE [bronze].[base_dato_actual_stage](
	-- 
	[FechaInventario] [varchar](max) NULL,
	[Proveedor] [varchar](max) NULL,
	[ModoPago] [varchar](max) NULL,
	[Linea] [varchar](max) NULL,
	[Referencia] [varchar](max) NULL,
	[InventarioInicial] [varchar](max) NULL,
	[CantidadEntrada] [varchar](max) NULL,
	[CantidadSalida] [varchar](max) NULL,
	[InventarioActual] [varchar](max) NULL,
	[UnidadMedida] [varchar](max) NULL,
	[CostoSinIVA] [varchar](max) NULL,
	[CostoConIVA] [varchar](max) NULL,
	[CostoTotal] [varchar](max) NULL
) 
GO

CREATE TABLE [bronze].[base_dato_entrada_stage] (
	-- [id] int identity(1,1) primary key not null,
    [FECHA]              VARCHAR(50),
    [NUMERO FACTURA]     VARCHAR(50),
    [PROVEEDOR]          VARCHAR(150),
    [REFERENCIA]         VARCHAR(150),
    [CANTIDAD]           VARCHAR(50),
    [U/M]                VARCHAR(20),
    [PRECIO UNITARIO]    VARCHAR(50),
    [PRECIO CON IVA]     VARCHAR(50),
    [PRECIO TOTAL]       VARCHAR(50)
);

go


CREATE TABLE [bronze].[base_dato_salida_stage] (
	-- [id] int identity(1,1) primary key not null,
    [CONSECUTIVO]           VARCHAR(50),
    [FECHA]                 VARCHAR(50),
    [CLIENTE INTERNO]       VARCHAR(150),
    [LOTE]                  VARCHAR(100),
    [REFERENCIA]            VARCHAR(150),
    [CANTIDAD]              VARCHAR(50),
    [U/M]                   VARCHAR(20),
    [COSTO CON IVA]         VARCHAR(50),
    [COSTO TOTAL SALIDA]    VARCHAR(50)
);
go



-- DATAWAREHOUSE TABLES 






CREATE TABLE [bronze].[base_dato_actual_dwh](
	-- 
	[FechaInventario] [varchar](max) NULL,
	[Proveedor] [varchar](max) NULL,
	[ModoPago] [varchar](max) NULL,
	[Linea] [varchar](max) NULL,
	[Referencia] [varchar](max) NULL,
	[InventarioInicial] [varchar](max) NULL,
	[CantidadEntrada] [varchar](max) NULL,
	[CantidadSalida] [varchar](max) NULL,
	[InventarioActual] [varchar](max) NULL,
	[UnidadMedida] [varchar](max) NULL,
	[CostoSinIVA] [varchar](max) NULL,
	[CostoConIVA] [varchar](max) NULL,
	[CostoTotal] [varchar](max) NULL,
	[id] int identity(1,1) primary key not null,
	[created_at] DATETIME default  SYSDATETIME(), 
	[bulk_block] int not null -- historical row bulk insert number block (1 for first bulk insert, 2 for second bulkinsert etc)
	) 
GO




CREATE TABLE [bronze].[base_dato_entrada_dwh] (
	-- [id] int identity(1,1) primary key not null,
    [FECHA]              VARCHAR(50),
    [NUMERO FACTURA]     VARCHAR(50),
    [PROVEEDOR]          VARCHAR(150),
    [REFERENCIA]         VARCHAR(150),
    [CANTIDAD]           VARCHAR(50),
    [U/M]                VARCHAR(20),
    [PRECIO UNITARIO]    VARCHAR(50),
    [PRECIO CON IVA]     VARCHAR(50),
    [PRECIO TOTAL]       VARCHAR(50),
	[id] int identity(1,1) primary key not null,
	[created_at] DATETIME default  SYSDATETIME(),
	[bulk_block] int not null -- historical row bulk insert number block (1 for first bulk insert, 2 for second bulkinsert etc)

	);

go






CREATE TABLE [bronze].[base_dato_salida_dwh] (
	-- [id] int identity(1,1) primary key not null,
    [CONSECUTIVO]           VARCHAR(50),
    [FECHA]                 VARCHAR(50),
    [CLIENTE INTERNO]       VARCHAR(150),
    [LOTE]                  VARCHAR(100),
    [REFERENCIA]            VARCHAR(150),
    [CANTIDAD]              VARCHAR(50),
    [U/M]                   VARCHAR(20),
    [COSTO CON IVA]         VARCHAR(50),
    [COSTO TOTAL SALIDA]    VARCHAR(50),
	[id] int identity(1,1) primary key not null,
	[created_at] DATETIME default  SYSDATETIME(),
	[bulk_block] int not null -- historical row bulk insert number block (1 for first bulk insert, 2 for second bulkinsert etc)

);
go






-- execute bronze.crawling_data_from_raw_files;

CREATE  PROCEDURE bronze.crawling_data_from_raw_files as

BEGIN

BEGIN TRY

DECLARE @bulk_block int; 

-- CLEANING STAGE TABLES 
  TRUNCATE TABLE  [Mobiliaria_carpintero_wh].[bronze].[base_dato_salida_stage];
  TRUNCATE TABLE [Mobiliaria_carpintero_wh].[bronze].[base_dato_actual_stage]; 
  TRUNCATE TABLE [Mobiliaria_carpintero_wh].[bronze].[base_dato_entrada_stage]; 
  --TRUNCATE TABLE  [Mobiliaria_carpintero_wh].[bronze].[base_dato_salida_dwh];
  --TRUNCATE TABLE [Mobiliaria_carpintero_wh].[bronze].[base_dato_actual_dwh]; 
  --TRUNCATE TABLE [Mobiliaria_carpintero_wh].[bronze].[base_dato_entrada_dwh]; 



BEGIN TRANSACTION; 
-- BULKING DATA FROM RAW FILES
--  TRUNCATE  TABLE [Mobiliaria_carpintero_wh].[bronze].[base_dato_entrada_dwh];


 BULK INSERT [Mobiliaria_carpintero_wh].[bronze].[base_dato_actual_stage]
FROM 'D:\mobiliaria_carpintero_raw_data\INVENTARIO ACTUAL ALMACEN 1(BASE DATO ACTUAL).csv'
WITH (
    FIRSTROW = 5,               -- Saltar filas basura
    FIELDTERMINATOR = ';',       -- Separador de columnas
    ROWTERMINATOR = '\n',        -- Fin de fila (Databricks / Linux)
    CODEPAGE = '65001',          -- UTF-8
    TABLOCK,
    KEEPNULLS
);



 BULK INSERT [Mobiliaria_carpintero_wh].[bronze].[base_dato_entrada_stage]
FROM 'D:\mobiliaria_carpintero_raw_data\INVENTARIO ACTUAL ALMACEN 1(BASE DATO ENTRADA ).csv'
WITH (
    FIRSTROW = 4,               -- Saltar filas basura
    FIELDTERMINATOR = ';',       -- Separador de columnas
    ROWTERMINATOR = '\n',        -- Fin de fila (Databricks / Linux)
    CODEPAGE = '65001',          -- UTF-8
    TABLOCK,
    KEEPNULLS
);


 BULK INSERT [Mobiliaria_carpintero_wh].[bronze].[base_dato_salida_stage]
FROM 'D:\mobiliaria_carpintero_raw_data\INVENTARIO ACTUAL ALMACEN 1(BASE DATO SALIDAS).csv'
WITH (
    FIRSTROW = 2,               -- Saltar filas basura
    FIELDTERMINATOR = ';',       -- Separador de columnas
    ROWTERMINATOR = '\n',        -- Fin de fila (Databricks / Linux)
    CODEPAGE = '65001',          -- UTF-8
    TABLOCK,
    KEEPNULLS
);


-- INSERTING DATA TO DWH TABLES

set @bulk_block = (select  top 1 ( isnull([bulk_block],0) +1) from [bronze].[base_dato_actual_dwh] with(tablockx) order by id desc);
if @bulk_block is null begin set @bulk_block = 1; end;


INSERT INTO [bronze].[base_dato_actual_dwh] ([FechaInventario]
      ,[Proveedor]
      ,[ModoPago]
      ,[Linea]
      ,[Referencia]
      ,[InventarioInicial]
      ,[CantidadEntrada]
      ,[CantidadSalida]
      ,[InventarioActual]
      ,[UnidadMedida]
      ,[CostoSinIVA]
      ,[CostoConIVA]
      ,[CostoTotal]
	  ,[bulk_block]
	  )
SELECT [FechaInventario]
      ,[Proveedor]
      ,[ModoPago]
      ,[Linea]
      ,[Referencia]
      ,[InventarioInicial]
      ,[CantidadEntrada]
      ,[CantidadSalida]
      ,[InventarioActual]
      ,[UnidadMedida]
      ,[CostoSinIVA]
      ,[CostoConIVA]
      ,[CostoTotal]
	  ,(@bulk_block)
  FROM [Mobiliaria_carpintero_wh].[bronze].[base_dato_actual_stage]; 

  

  

  



 
  INSERT INTO [bronze].[base_dato_entrada_dwh] ([FECHA]
      ,[NUMERO FACTURA]
      ,[PROVEEDOR]
      ,[REFERENCIA]
      ,[CANTIDAD]
      ,[U/M]
      ,[PRECIO UNITARIO]
      ,[PRECIO CON IVA]
      ,[PRECIO TOTAL]
	  ,[bulk_block]
	  ) 
  SELECT[FECHA]
      ,[NUMERO FACTURA]
      ,[PROVEEDOR]
      ,[REFERENCIA]
      ,[CANTIDAD]
      ,[U/M]
      ,[PRECIO UNITARIO]
      ,[PRECIO CON IVA]
      ,[PRECIO TOTAL]
	  ,(@bulk_block)

  FROM [Mobiliaria_carpintero_wh].[bronze].[base_dato_entrada_stage]; 

  



  INSERT INTO [bronze].[base_dato_salida_dwh](
	   [CONSECUTIVO]
      ,[FECHA]
      ,[CLIENTE INTERNO]
      ,[LOTE]
      ,[REFERENCIA]
      ,[CANTIDAD]
      ,[U/M]
      ,[COSTO CON IVA]
      ,[COSTO TOTAL SALIDA]
	  ,[bulk_block]
	  )
  SELECT[CONSECUTIVO]
      ,[FECHA]
      ,[CLIENTE INTERNO]
      ,[LOTE]
      ,[REFERENCIA]
      ,[CANTIDAD]
      ,[U/M]
      ,[COSTO CON IVA]
      ,[COSTO TOTAL SALIDA]
	  ,(@bulk_block)

  FROM  [Mobiliaria_carpintero_wh].[bronze].[base_dato_salida_stage];



  COMMIT TRANSACTION; 




  BEGIN TRANSACTION;

-- deleting full null row from tables

with hashtable as (
SELECT 
hashbytes('SHA2_256',concat(
		[FechaInventario]
      ,[Proveedor]
      ,[ModoPago]
      ,[Linea]
      ,[Referencia]
      ,[InventarioInicial]
      ,[CantidadEntrada]
      ,[CantidadSalida]
      ,[InventarioActual]
      ,[UnidadMedida]
      ,[CostoSinIVA]
      )) as hash1, id 
    
  FROM [Mobiliaria_carpintero_wh].[silver].[base_dato_actual_vw] )   -- 0xE3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855 -- null hash

  delete from [Mobiliaria_carpintero_wh].[silver].[base_dato_actual_vw] where id in (
  select id from hashtable where hash1 = cast(0xE3B0C44298FC1C149AFBF4C8996FB92427AE41E4649B934CA495991B7852B855 as varbinary(32)));



  -- base dato salida



  with hash_table2 as(
  SELECT HASHBYTES('SHA2_256', CONCAT([CONSECUTIVO]
      ,[FECHA]
      ,[CLIENTE INTERNO]
      ,[LOTE]
      ,[REFERENCIA]
      ,[CANTIDAD]
      ,[U/M]
      ,[COSTO CON IVA]
      ,[COSTO TOTAL SALIDA])) as hashs, id
  
  FROM [Mobiliaria_carpintero_wh].[silver].[base_dato_salida_vw] -- 0x5FECEB66FFC86F38D952786C6D696C79C2DBC239DD4E91B46729D73A27FB57E9
  )
  delete from [Mobiliaria_carpintero_wh].[silver].[base_dato_salida_vw] where id in (
  select id  from hash_table2 where hashs = cast(0x5FECEB66FFC86F38D952786C6D696C79C2DBC239DD4E91B46729D73A27FB57E9 as varbinary(32)));





  COMMIT;






END TRY
BEGIN CATCH

THROW; 

END CATCH;


END;



-- creating views for silver layer 
CREATE VIEW  silver.[base_dato_actual_vw] as 
SELECT  CONVERT(DATE,[FechaInventario],103)as 
[FechaInventario]
      ,[Proveedor]
      ,[ModoPago]
      ,[Linea]
      ,[Referencia]
       ,try_cast(REPLACE([InventarioInicial],',','.') as float) as [InventarioInicial]
	  
      ,try_cast(REPLACE([CantidadEntrada],',','.') as float) as [CantidadEntrada]
      ,try_cast(REPLACE([CantidadSalida],',','.') as float) as [CantidadSalida]
      ,try_cast(REPLACE([InventarioActual],',','.') as float) as [InventarioActual]
      ,[UnidadMedida]
      ,replace(replace([CostoSinIVA],'$',''),'.','') as [CostoSinIVA]
      ,replace(replace([CostoConIVA], '$',''),'.','') as [CostoConIVA]
      ,replace(replace(replace([CostoTotal], '$',''),'.',''),';','')  as [CostoTotal]
      ,[id]
      ,[created_at]
      ,[bulk_block]
  FROM [Mobiliaria_carpintero_wh].[bronze].[base_dato_actual_dwh]; 




CREATE VIEW  silver.[base_dato_entrada_vw] as 

SELECT CONVERT(date,[FECHA], 103) AS [FECHA]
      ,[NUMERO FACTURA]
      ,[PROVEEDOR]
      ,[REFERENCIA]
      , TRY_CAST(REPLACE([CANTIDAD], ',','.') AS FLOAT ) AS [CANTIDAD]
      ,[U/M]
      ,try_CAST(REPLACE(REPLACE(REPLACE([PRECIO UNITARIO],',','.'),'.',''),'$','')  AS FLOAT) AS [PRECIO UNITARIO]
      , try_CAST(REPLACE(REPLACE(REPLACE([PRECIO CON IVA],',','.'),'.',''),'$','') AS float)AS [PRECIO CON IVA]
      , try_CAST(REPLACE(REPLACE(REPLACE(REPLACE([PRECIO TOTAL],',','.'),'.',''),'$',''),';','')  AS FLOAT)AS  [PRECIO TOTAL]
      ,[id]
      ,[created_at]
      ,[bulk_block]
  FROM [Mobiliaria_carpintero_wh].[bronze].[base_dato_entrada_dwh]; 



CREATE VIEW silver.[base_dato_salida_vw] as 
SELECT  [CONSECUTIVO]
      ,convert(date,[FECHA],103) as [FECHA]
      ,[CLIENTE INTERNO]
      ,[LOTE]
      ,[REFERENCIA]
      ,TRY_CAST(REPLACE([CANTIDAD], ',','.') AS FLOAT ) AS [CANTIDAD]
      ,[U/M]
      ,try_CAST(REPLACE(REPLACE(REPLACE([COSTO CON IVA],',','.'),'.',''),'$','') AS float)AS [COSTO CON IVA]
      ,try_CAST(REPLACE(REPLACE(REPLACE(REPLACE([COSTO TOTAL SALIDA],',','.'),'.',''),'$',''),';','')  AS FLOAT)AS[COSTO TOTAL SALIDA]
      ,[id]
      ,[created_at]
      ,[bulk_block]
  FROM [Mobiliaria_carpintero_wh].[bronze].[base_dato_salida_dwh];







  -- Gold layer

  -- calculate the  initial inventory  (UpToDate)

   create or alter view gold.inventarioinicial as select cast(SUM(InventarioInicial) as int) as InventarioInicial, sum(InventarioActual) as cant_productos_actual from [silver].[base_dato_actual_vw]; 

 


 -- get total cost of inventory

  CREATE OR ALTER VIEW gold.costo_inventario_inicial as 
  -- query to get the most recently products' price
  WITH precio_referencia as ( select DISTINCT [REFERENCIA] , [FECHA],[PRECIO CON IVA],[CANTIDAD] , 
  ROW_NUMBER() over(partition by referencia order by fecha asc)  as max_fecha from [silver].[base_dato_entrada_vw] )
  
   ,max_ref as (
   select referencia,MAX(max_fecha) as mxs from precio_referencia group by referencia
   )

   select--  mx.referencia,pr.[PRECIO CON IVA], pr.fecha, mx.mxs, pr.max_fecha --, sum(slv.InventarioInicial)  as InventarioInicial , 
  sum( (slv.InventarioInicial * [PRECIO CON IVA])) AS costo_inventario_inicial-- , sum(slv.InventarioInicial) as InventarioInicial
   from max_ref  as mx left join precio_referencia as pr on mx.mxs = pr.max_fecha and mx.referencia = pr.referencia
   INNER  join [silver].[base_dato_actual_vw] as slv on slv.Referencia = mx.referencia; 




   -- Get total stock buy inbound by most recently buy 
CREATE OR ALTER VIEW gold.cantidad_entradas_by_lasDate as 
   WITH cantidad_view as (
select  FECHA, REFERENCIA,CANTIDAD, [PRECIO CON IVA] , row_number() over(partition by REFERENCIA order by FECHA desc) AS position -- , SUM(CANTIDAD) as total_entradas 
from [silver].[base_dato_entrada_vw]  ) 

select sum(CANTIDAD) as cantidad_entrada, SUM([PRECIO CON IVA]) AS money_total from cantidad_view where position = 1; 


CREATE  or alter VIEW gold.cantidad_salidas_prices_total as 
select cast(sum(CANTIDAD) as numeric(10,2)) as salidas_cantidad, sum([COSTO TOTAL SALIDA]) as costo_total_salida from [silver].[base_dato_salida_vw];


CREATE or alter VIEW gold.stock_minimo_maximo_seguridad_cant_products as 

-- CALCULATE MINIMUM STOCK BY PRODUCTS
-- tome la bd salida porque es lo que mas se asemeja a la cantidad de compras por dia y consumo de materiales por dia
with promedio as (
select REFERENCIA, cast ( avg(CANTIDAD) as numeric(10,2))as promedio_consumo from [silver].[base_dato_salida_vw] group by REFERENCIA), stock_minimo as (

select promedio.REFERENCIA,promedio.promedio_consumo,(3 /*tiempo de entrega*/ * promedio.promedio_consumo) as STOCK_MINIMO , bda.InventarioActual as cantidad_producto
from promedio inner join silver.base_dato_actual_vw as bda on bda.Referencia = promedio.REFERENCIA ) 


select REFERENCIA, STOCK_MINIMO, (STOCK_MINIMO*2) AS STOCK_MAXIMO,( STOCK_MINIMO + ((7 /*tiempo de retraso*/-3 /*tiempo de entrega*/) *promedio_consumo ) ) as STOCK_DE_SEGURIDAD , cantidad_producto FROM stock_minimo;


-- STOCK MAXIMO 
 











