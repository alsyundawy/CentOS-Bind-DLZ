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

BuildRequires:  krb5-devel
BuildRequires:  libcap
BuildRequires:  libcap-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  openldap
BuildRequires:  openldap-devel
BuildRequires:  openssl
BuildRequires:  openssl-devel
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  libxslt docbook-style-xsl
BuildRequires:  autoconf pkgconfig libtool net-tools  byacc shadow-utils coreutils
BuildRequires:  libidn-devel
BuildRequires:  python-argparse python-argcomplete python-argh
BuildRequires:  opensc pkcs11-helper pkcs11-helper-devel
BuildRequires:  db4-devel

