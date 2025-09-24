########################### QUERY ORIGINAL COUSING BOTTLENECKS ON THE PRODUCTION SERVER ##############################
-- PROCESANDO  ALREDEDOR DE UN AÑO DE INFORMACION
-- EXECUTION TIME FOR THIS QUERY: 211 SECS + ERROR LOST CONECTION DEBIDO A RESTRICCIONES DE QUERY TIME DEL SERVIDOR MYSQL


use nc_tecnoesw_db;

-- EXPLAIN 
 -- EJEMPLO CON FILTRO DE FECHA > '2024-09-12'

SELECT 
    res.fecha,
    res.cantidad,
    res.Solucionadas,
    (res.cantidad - res.Solucionadas) AS pendientes
FROM
    (
    
    
    
    SELECT 
        SUBSTR(fecha, 1, 10) AS fecha,
            COUNT(*) AS cantidad,
            
            
            (SELECT 
                    COUNT(*)
                FROM
                    nc_tecnoesw_db.nc_aluminio a2
                WHERE
                    SUBSTR(a1.fecha, 1, 10) = SUBSTR(a2.fecha, 1, 10)
                        AND a2.id_estado IN (3)) Solucionadas
                        
                        
    FROM
        nc_tecnoesw_db.nc_aluminio a1
    WHERE
        SUBSTR(a1.fecha, 1, 10) > '2024-09-12'
            AND a1.id_estado NOT IN (5)
    GROUP BY SUBSTR(a1.fecha, 1, 10)
    ORDER BY fecha
    
    
    
    ) AS res
WHERE
    (res.cantidad - res.Solucionadas) > 0; 
    
    
    
    
########################### QUERY OPTIMIZED BY DIDIER A ##############################
-- PROCESANDO  ALREDEDOR DE UN AÑO DE INFORMACION
-- EXECUTION TIME FOR THIS QUERY:  0.782 SECS 


    
    -- EXPLAIN 
    
    with a1 as ( 
    
     select convert(a1.fecha , date) as fecha , a1.id_estado from  nc_tecnoesw_db.nc_aluminio a1  WHERE
        a1.fecha > '2024-09-12'   
        and a1.id_estado   not in(5)  -- se queda como clausula de rango debido a que este query desde el backend siempre recibe listas de > 3 tipos de estados 
        
        
        ) , Solucionadas as (
        
         select count(0) as solucionadas,fecha from a1 where id_estado in(3) group by fecha
        
        
        ), pendientes as (
        
        select a1.fecha,count(0) as cantidad,s.solucionadas  from a1 inner join Solucionadas as s  on a1.fecha=s.fecha group by a1.fecha
        
        )
        
        select t.*,(t.cantidad - t.solucionadas) as pendientes  from pendientes t  having pendientes > 0;
        
    
        
        
    
    
    
