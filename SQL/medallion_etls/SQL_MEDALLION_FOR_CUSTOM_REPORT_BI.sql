-- MEDALLION ARQUITECTURE, CALLS 3CX PROJECT.

-- Table: public.cdroutput

-- DROP TABLE IF EXISTS public.cdroutput;


-- FIRST STEP: CREATE BRONZE LAYER (RAW DATA).
-- THIS TABLE IS CREATED FOR SAVE ALL THE DATA FROM SOURCES FILES, THAT FILES ARE IMPORTED FROM APLICATION 3CX AUTOMATIC EXPORT DATA.
CREATE TABLE IF NOT EXISTS public.cdroutput
(
    cdr_id uuid,
    call_history_id uuid,
    source_participant_id uuid,
    source_entity_type character varying COLLATE pg_catalog."default",
    source_dn_number character varying COLLATE pg_catalog."default",
    source_dn_type character varying COLLATE pg_catalog."default",
    source_dn_name character varying COLLATE pg_catalog."default",
    source_participant_name character varying COLLATE pg_catalog."default",
    source_participant_phone_number character varying COLLATE pg_catalog."default",
    source_participant_trunk_did character varying COLLATE pg_catalog."default",
    source_participant_is_incoming boolean,
    source_participant_is_already_connected boolean,
    source_participant_group_name character varying COLLATE pg_catalog."default",
    source_participant_billing_suffix character varying COLLATE pg_catalog."default",
    destination_participant_id uuid,
    destination_entity_type character varying COLLATE pg_catalog."default",
    destination_dn_number character varying COLLATE pg_catalog."default",
    destination_dn_type character varying COLLATE pg_catalog."default",
    destination_dn_name character varying COLLATE pg_catalog."default",
    destination_participant_name character varying COLLATE pg_catalog."default",
    destination_participant_phone_number character varying COLLATE pg_catalog."default",
    destination_participant_trunk_did character varying COLLATE pg_catalog."default",
    destination_participant_is_incoming boolean,
    destination_participant_is_already_connected boolean,
    destination_participant_group_name character varying COLLATE pg_catalog."default",
    destination_participant_billing_suffix character varying COLLATE pg_catalog."default",
    base_cdr_id uuid,
    originating_cdr_id uuid,
    creation_method character varying COLLATE pg_catalog."default",
    creation_forward_reason character varying COLLATE pg_catalog."default",
    termination_reason character varying COLLATE pg_catalog."default",
    terminated_by_participant_id uuid,
    continued_in_cdr_id uuid,
    cdr_started_at timestamp with time zone,
    cdr_ended_at timestamp with time zone,
    cdr_answered_at timestamp with time zone,
    termination_reason_details character varying COLLATE pg_catalog."default",
    processed boolean,
    migrated boolean,
    main_call_history_id uuid,
    source_presentation character varying COLLATE pg_catalog."default",
    offload_id bigint
)
WITH (
    OIDS = FALSE
)
TABLESPACE pg_default;





-- SECOND STEP: CREATE SILVER LAYER (CLEANISING THE DATA, DATA ENRICHMENT).
-- THIS TABLE ARE CREATED FOR SAVE ALL THE DATA FROM SOURCES FILES, THAT FILES ARE IMPORTED FROM APLICATION 3CX AUTOMATIC EXPORT DATA.

-- CREATE SCHEMA: 
CREATE SCHEMA IF NOT EXISTS silver;
-- CREATE EXTENSION pgcrypto for generate random uuid
CREATE EXTENSION IF NOT EXISTS pgcrypto;


-- CREATE TABLE SILVER LAYER



CREATE TABLE silver.calls_output_report(
silver_call_id uuid primary key DEFAULT gen_random_uuid(),
cdr_id uuid, 
cdr_started_at timestamp, 
from_source varchar,
too varchar,
extension_ varchar, 
status varchar, 
to_vom varchar,
cdr_ended_at timestamp, 
call_time numeric(100,2)
);

-- INGEST DATA  TO SILVER LAYER

INSERT INTO silver.calls_output_report(cdr_id,cdr_started_at,from_source,too,extension_,status,to_vom,cdr_ended_at,call_time)

select cdr_id ,
cdr_started_at as "started_at", 
source_participant_phone_number as "from_source",
destination_dn_name  as "too", 
destination_dn_number as "extension_",
case when cdr_answered_at is not null then 'Asnwered' when  cdr_answered_at is null then 'Unanswered' end as "status",
destination_entity_type as "to_vom",
cdr_ended_at,
(extract(EPOCH FROM (cdr_ended_at  - cdr_started_at)) / 60 )::numeric(100,2) as call_time


from public.cdroutput 

-- CREATE INDEX OVER BRONZE TABLE 
CREATE INDEX idx_bronze_created_at
ON public.cdroutput (created_at);

-- select (current_timestamp - interval '1 day') as date_begin


-- CREATE GOLD LAYER  
CREATE SCHEMA gold; 

-- CREATED MATERIALIZED VIEW FROM SILVER 

CREATE MATERIALIZED VIEW gold.calls_output_gold as select * from gold.calls_output_gold;

-- COPYING FILE TO CSV FOR BETTER MANAGEMENT IN DIFERENTS DATA SOURCES(CONVERTO TO PARQUET USING SPARK, DATAFRAMES ETC)
COPY  (select * from gold.calls_output_gold) TO '/data/postgresql/10/main/gold_layer.csv' with (FORMAT CSV, HEADER, DELIMITER ',', NULL '');













