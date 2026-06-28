select sucursal, sum(cantidad) as transacciones, sum(total) as total_ventas  from ventas 
where precio_unit <> 0 and cantidad is not null and cantidad <> 0 and sucursal is not null
group by sucursal
order by transacciones desc
;
select sucursal, sum(cantidad) as transacciones, sum(total) as total_ventas  from ventas 
where precio_unit <> 0 and cantidad is not null and cantidad <> 0 and sucursal is not null
group by sucursal
;
select top 1 producto, sum(cantidad) as cant from ventas
where precio_unit <> 0 and cantidad is not null and cantidad <> 0 and sucursal is not null and producto is not null
group by producto
order by cant desc;
--query 3
select month(fecha) ,datename(month, fecha) as mes,  count(*), sum (total) from ventas
group by datename(month, fecha), month(fecha)
order by month(fecha)
;
--query 4
select top 1 sucursal, avg(precio_unit) as prom_precio from ventas
where sucursal is not null
group by sucursal
order by prom_precio desc
;
--query 5
select count(*) from ventas
where fecha is null or sucursal is null or producto is null
or cantidad is null or precio_unit is null or total is null
or cantidad <= 0 or precio_unit <=0