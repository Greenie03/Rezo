$TTL	60000
@		IN	SOA	dnscom.com.	root.dnscom.com. (
			1 ; serial
			28 ; refresh
			14 ; retry
			3600000 ; expire
			60000 ; negative cache ttl
			)
@		IN	NS	dnscom.com.
dnscom		IN	A	30.40.50.253

notascam		IN	NS	dnsnot.com.
dnsnot			IN	A	81.82.83.2

sillymail		IN	NS	dnsres.sillymail.com
dnsres.sillymail	IN	A	20.30.40.50
