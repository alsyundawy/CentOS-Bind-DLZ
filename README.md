CentOS-Bind-DLZ
===============

Build Project für Bind 9 Nameserver with DLZ for samab4-dlz 

Flexible Build SPEC for Centos / FC / redhat .
<pre>
root@centosdev1:log#  named-sdb -V
BIND 9.9.6-Remsnet_LTD-9.9.6-4.el6 (Extended Support Version) <id:ea4e9ef8> built by make with '--build=x86_64-redhat-linux-gnu' '--program-prefix=' '--exec-prefix=/usr' '--includedir=/usr/include' '--prefix=/usr' '--bindir=/usr/bin' '--sbindir=/usr/sbin' '--sharedstatedir=/var/lib' '--libexecdir=/usr/libexec' '--localstatedir=/var' '--includedir=/usr/include/bind9' '--libdir=/usr/lib64' '--datadir=/usr/share' '--mandir=/usr/share/man' '--infodir=/usr/share/info' '--docdir=/usr/share/doc' '--sysconfdir=/etc' '--host=x86_64-redhat-linux-gnu' '--target=x86_64-redhat-linux-gnu' '--with-docbook-xsl=/usr/share/sgml/docbook/xsl-stylesheets' '--enable-newstats' '--disable-static' '--enable-exportlib' '--with-export-libdir=/usr/lib64' '--with-export-includedir=/usr/include' '--with-openssl' '--enable-threads' '--disable-openssl-version-check' '--with-libtool' '--with-pic' '--with-python' '--with-dlopen=yes' '--with-dlz-ldap=yes' '--with-dlz-filesystem=yes' '--with-dlz-bdb=yes' '--with-gssapi=yes' '--with-idnlib=-L/usr/lib -R/usr/lib -lidn -lidn2' '--with-libxml2' '--enable-filter-aaaa' '--enable-rrl' '--with-ecdsa' '--enable-fixed-rrset' 'build_alias=x86_64-redhat-linux-gnu' 'host_alias=x86_64-redhat-linux-gnu' 'target_alias=x86_64-redhat-linux-gnu' 'CC=gcc' 'CFLAGS=-O2 -g -DNO_VERSION_DATE -fno-strict-aliasing -fpie ' 'LDFLAGS=-L/usr/lib64 -L/usr/lib64/mysql -pie' 'CPPFLAGS= -DDIG_SIGCHASE'
compiled by GCC 4.4.7 20120313 (Red Hat 4.4.7-11)
using OpenSSL version: OpenSSL 1.0.1e 11 Feb 2013
using libxml2 version: 2.7.6
root@centosdev1:log#
</pre>




reason for this RPM BUild Project :
 - Centos / FC / RedHat  current distributed BIND9 rpms have not all required options service signed dns updates:
    *   SPNEGO are disabled
    *   BDB don´t work
    *   DL open allmost disabled.
    *   IDN not enabled
    *   Samba4 internal dns lacs still some standard featgers that Bind9 provide.

Thus the distributed Centos / FC / RedHat BIND9 RPMS are allmost Incompatible with the Modern samba 4.1.2 and up.



RPMS , SRPM Files of this CentOS-Bind-DLZ
 are stored on Our Drop box url :

Current of this Samba4-DC Build are stored on Our Drop box url : https://www.dropbox.com/sh/p4ijdacy90xebqk/4moyZY9Ne8 Currently 
RPMS are created for : 


 Wrote: /root/rpmbuild/SRPMS/bind-9.9.6-4.el6.src.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-devel-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-lite-devel-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-sdb-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-libs-lite-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/noarch/bind-license-9.9.6-4.el6.noarch.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-doc-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-libs-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-lwresd-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-utils-9.9.6-4.el6.x86_64.rpm <br>
 Wrote: /root/rpmbuild/RPMS/x86_64/bind-chroot-9.9.6-4.el6.x86_64.rpm <br>


