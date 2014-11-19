CentOS-Bind-DLZ
===============

Build Project für Bind 9 Nameserver with DLZ for samab4-dlz 

Flexible Build SPEC for Centos / FC / redhat .

reason for this RPM BUild Project :
 - Centos / FC / RedHat  current distributed BIND9 rpms have not all required options service signed dns updates:
    *   SPNEGO are disabled
    *   BDB don´t work
    *   DL open allmost disabled.
    *   IDN not enabled
    *   Samba4 internal dns lacs still some standard featgers that Bind9 provide.

Thus the distributed Centos / FC / RedHat BIND9 RPMS are allmost Incompatible with the Modern samba 4.1.2 and up.

