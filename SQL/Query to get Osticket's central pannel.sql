/*Query to get Osticket's central pannel*/
use osticket_db; 

SELECT 
    ost_ticket.`Ticket`,
    ost_ticket.`Last Updated`,
    ost_ticket.`Subject`,
    ost_ticket.`From`,
    ost_ticket.`Priority`,
    CASE
        WHEN ost_ticket.staff_id = 0 THEN ost_team.name
        ELSE CONCAT(ost_staff.username,
                ' ',
                ost_staff.firstname,
                ' ',
                ost_staff.lastname)
    END AS `Assigned To`
FROM
    (SELECT 
        ost_ticket.number AS `Ticket`,
            ost_ticket.lastupdate AS `Last Updated`,
            ost_ticket__cdata.subject AS `Subject`,
            ost_user.name AS `From`,
            osticket_db.ost_ticket_priority.priority AS `Priority`,
            ost_ticket.staff_id,
            ost_ticket.team_id
    FROM
        ost_thread
    INNER JOIN ost_ticket ON ost_thread.object_id = ost_ticket.ticket_id
    INNER JOIN ost_user ON ost_user.id = ost_ticket.user_id
    INNER JOIN ost_ticket__cdata ON ost_ticket.ticket_id = ost_ticket__cdata.ticket_id
    INNER JOIN osticket_db.ost_ticket_priority ON osticket_db.ost_ticket_priority.priority_id = ost_ticket__cdata.priority
    INNER JOIN ost_thread_entry ON ost_thread_entry.thread_id = ost_thread.id
     WHERE
     ost_thread_entry.user_id != 0   and ost_ticket.created > date_sub(now() , interval 1 day)
	 -- and  ost_ticket.number = 952275
    -- ORDER BY ost_thread_entry.id DESC
    ) AS ost_ticket
        LEFT JOIN
    ost_staff ON ost_staff.staff_id = ost_ticket.staff_id
        LEFT JOIN
    ost_team ON ost_team.team_id = ost_ticket.team_id 
    order by  ost_ticket.`Last Updated` desc;

/**
select * 
FROM
        ost_thread
    INNER JOIN ost_ticket ON ost_thread.object_id = ost_ticket.ticket_id
     INNER JOIN ost_user ON ost_user.id = ost_ticket.user_id
    INNER JOIN ost_ticket__cdata ON ost_ticket.ticket_id = ost_ticket__cdata.ticket_id
    INNER JOIN osticket_db.ost_ticket_priority ON osticket_db.ost_ticket_priority.priority_id = ost_ticket__cdata.priority
    INNER JOIN ost_thread_entry ON ost_thread_entry.thread_id = ost_thread.id
     WHERE
         ost_ticket.number = 203854
         
  /**       
select * from ost_user where id = 612         
select * from ost_ticket where number =  952275;
select * from ost_thread where object_id = 71015;
select * from ost_thread_entry where  thread_id =  71401
select * from ost_ticket__cdata where ticket_id = 71015
select * from osticket_db.ost_ticket_priority where priority_id = 2 

**/