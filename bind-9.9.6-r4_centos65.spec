#
# spec v0.6 file for package bind-9.9.6-r4
#
# Copyright (c) 1995-2014 Remsnet Consulting & Internet Services LTD
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://github.com/remsnet/Centos6-BIND9-DLZ/blob/master/bind-9.9.6-r3.spec

%{?!SDB:       %define SDB       1}
%{?!BDB:       %define BDB       1}
%{?!MYSQLDB:   %define MYSQLDB   0}
%{?!IDN:       %define IDN       1}
%{?!test:      %define test      0}
%{?!bind_uid:  %define bind_uid  25}
%{?!bind_gid:  %define bind_gid  25}
%{?!GSSTSIG:   %define GSSTSIG   1}
%{?!PKCS11:    %define PKCS11    0}
%{?!DEVEL:     %define DEVEL    1}
%define        bind_dir          /var/named
%define        chroot_prefix     %{bind_dir}/chroot
#
# for disable spnego set 1
%{?!SPNEGO:    %define SPNEGO    0}

%define PATCHVER 0
%define NAME bind
%define name %{NAME}
%define version 9.9.6
%define release 4
%define VER %{version}

# Defines for user and group add
%define NAMED_UID %bind_uid
%define NAMED_UID_NAME named
%define NAMED_GID %bind_gid
%define NAMED_GID_NAME named
%define NAMED_COMMENT Name server daemon
%define NAMED_HOMEDIR /var/named
%define NAMED_SHELL /sbin/nologin
%define GROUPADD_NAMED /usr/sbin/groupadd -g %{NAMED_GID} -o -r %{NAMED_GID_NAME} 2> /dev/null || :
%define USERADD_NAMED /usr/sbin/useradd -r -o -g %{NAMED_GID_NAME} -u %{NAMED_UID} -s %{NAMED_SHELL} -c "%{NAMED_COMMENT}" -d %{NAMED_HOMEDIR} %{NAMED_UID_NAME} 2> /dev/null || :
%define USERMOD_NAMED /usr/sbin/usermod -s %{NAMED_SHELL} -d  %{NAMED_HOMEDIR} %{NAMED_UID_NAME} 2>/dev/null || :
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


Name:           %{NAME}
%define pkg_name %{NAME}
%define pkg_vers %{VER}
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
Summary:        Domain Name System (DNS) Server (named)
License:        ISC
Group:          Productivity/Networking/DNS/Servers
Version:        %{version}
Release:        %{release}%{?dist}
Provides:       named
Provides:       bind9
Provides:       dns_daemon
Provides:       name_server nameserver
Obsoletes:      bind8 bind4
Obsoletes:      bind9
Requires:       %{NAME}-chroot
Requires:       %{NAME}-utils
Url:            http://isc.org/sw/bind/
Packager:       Horst Venzke <horst.venzke@remsnet.de>
Source:   ftp://ftp.isc.org/isc/bind9/%{VER}/bind-%{VER}.tar.gz
Source1:  named.sysconfig
Source2:  named.init
Source3:  named.logrotate
Source4:  named.NetworkManager
Source5:  rfc1912.txt
Source6:  named.portreserve
Source7:  bind-9.3.1rc1-sdb_tools-Makefile.in
Source8:  dnszone.schema
Source9:  dlz-schema.txt
Source10: bind.tmpfiles.d
Source12: README.sdb_pgsql
Source21: Copyright.caching-nameserver
#
Source28: bind9-config.tar.bz2
#
Source30: ldap2zone.c
Source31: ldap2zone.1
Source32: named-sdb.8
Source33: zonetodb.1
Source34: zone2sqlite.1
Source35: bind.tmpfiles.d
Source36: trusted-key.key

# Common patches
Patch5:  bind-nonexec.patch
Patch10: bind-9.5-PIE.patch
Patch16: bind-9.3.2-redhat_doc.patch
Patch71: bind-9.5-overflow.patch
Patch72: bind-9.5-dlz-64bit.patch
Patch87: bind-9.5-parallel-build.patch
Patch99: bind-96-libtool2-9.9.3.patch
Patch101:bind-96-old-api.patch
Patch102:bind-95-rh452060.patch
Patch106:bind93-rh490837.patch
Patch107:bind97-dist-pkcs11.patch
Patch109:bind97-rh478718.patch
Patch110:bind97-rh570851-995.patch
Patch111:bind97-exportlib-9.9.3.patch
Patch112:bind97-rh645544-994.patch
Patch117:bind98-rh725741.patch
Patch118:bind97-rh699951.patch
Patch119:bind97-rh693982.patch
Patch120:bind97-rh700097.patch
Patch121:bind97-rh714049-9.9.5.patch
Patch122:bind98-dlz_buildfix-996.patch
Patch123:bind98-rh735103.patch

# SDB patches
Patch11: bind-9.3.2b2-sdbsrc.patch
Patch12: bind-9.5-sdb-9.9.3-P1.patch
Patch62: bind-9.5-sdb-sqlite-bld.patch

# needs inpection
Patch17: bind-9.3.2b1-fix_sdb_ldap.patch
Patch104: bind-96-dyndb.patch

# IDN paches
Patch73: bind-9.5-libidn.patch
Patch83: bind-9.5-libidn2.patch
Patch85: bind-9.5-libidn3.patch
Patch94: bind95-rh461409.patch

# Comment from atkac:
#
# Don't extract provides for the following libraries. Non-BIND9
# applications should not use them, they should use libraries
# from bind-libs-lite package.
#
# Since bind-libs-lite doesn't contain some libraries used by all
# BIND9 programs (like liblwres) use those "internal" libraries for
# dependency resolution. If, for example, bind package requires
# libdns.so then it will automatically pull in both bind-libs
# and bind-libs-lite (which is incorrect, only bind-libs is needed)
%{?filter_setup:
%filter_provides_in %{_libdir}/bind9/libdns\.so.*
%filter_provides_in %{_libdir}/bind9/libisc\.so.*
%filter_provides_in %{_libdir}/bind9/libisccfg\.so.*
%filter_from_requires /libdns\.so.*/d
%filter_from_requires /libisc\.so.*/d
%filter_from_requires /libisccfg\.so.*/d
%filter_setup
}



%description
Berkeley Internet Name Domain (BIND) is an implementation of the Domain
Name System (DNS) protocols and provides an openly redistributable
reference implementation of the major components of the Domain Name
System.  This package includes the components to operate a DNS server.

%if %{DEVEL}
%package devel
Summary:        Development Libraries and Header Files of BIND
Group:          Development/Libraries/C and C++
Requires:       %{NAME}-libs = %{version}
Provides:       bind8-devel
Provides:       bind9-devel
Obsoletes:      bind8-devel
Obsoletes:      bind9-devel

%description devel
This package contains the header files, libraries, and documentation
for building programs using the libraries of the Berkeley Internet Name
Domain (BIND) Domain Name System implementation of the Domain Name
System (DNS) protocols.
%endif

%package lite-devel
Summary:  Lite version of header files and libraries needed for BIND DNS development
Group:    Development/Libraries
Requires: bind-libs-lite = %{epoch}:%{version}-%{release}

%description lite-devel
The bind-lite-devel package contains lite version of the header
files and libraries required for development with ISC BIND 9



%if %{SDB}
%package sdb
Summary: BIND server with database backends and DLZ support
Group:   System Environment/Daemons
Requires:bind-libs = %{version}-%{release}
Requires:bind-license = %{version}-%{release}

%description sdb
BIND (Berkeley Internet Name Domain) is an implementation of the DNS
(Domain Name System) protocols. BIND includes a DNS server (named-sdb)
which has compiled-in SDB (Simplified Database Backend) which includes
support for using alternative Zone Databases stored in an LDAP server
(ldapdb), a postgreSQL database (pgsqldb), an sqlite database (sqlitedb),
or in the filesystem (dirdb), in addition to the standard in-memory RBT
(Red Black Tree) zone database. It also includes support for DLZ
(Dynamic Loadable Zones)
%endif

%package libs-lite
Summary:  Libraries for working with the DNS protocol
Group:    Applications/System
Obsoletes:bind-libbind-devel < 9.3.3-4.fc7
Provides: bind-libbind-devel = 9.3.3-4.fc7
Requires: bind-license = %{version}-%{release}

%description libs-lite
Contains lite version of BIND suite libraries which are used by various
programs to work with DNS protocol.

%package license
Summary:  License of the BIND DNS suite
Group:    Applications/System
BuildArch:noarch

%description license
Contains license of the BIND DNS suite.


%if %{PKCS11}
%package pkcs11
Summary: Bind PKCS#11 tools for using DNSSEC
Group:   System Environment/Daemons
Requires: opensc pkcs11-helper
BuildRequires: pkcs11-helper-devel
Requires:bind-license = %{version}-%{release}

%description pkcs11
This is a set of PKCS#11 utilities that when used together create rsa
keys in a PKCS11 keystore, such as provided by opencryptoki. The keys
will have a label of "zone,zsk|ksk,xxx" and an id of the keytag in hex.
%endif

%package doc
Summary:        BIND documentation
Group:          Documentation/Other
Requires:bind-license = %{version}-%{release}

%description doc
Documentation of the Berkeley Internet Name Domain (BIND) Domain Name
System implementation of the Domain Name System (DNS) protocols.  This
includes also the BIND Administrator Reference Manual (ARM).

%package libs
Summary:        Shared libraries of BIND
Group:          Development/Libraries/C and C++
Requires:bind-license = %{version}-%{release}

%description libs
This package contains the shared libraries of the Berkeley Internet
Name Domain (BIND) Domain Name System implementation of the Domain Name
System (DNS) protocols.

%package lwresd
Summary:        Lightweight Resolver Daemon
Group:          Productivity/Networking/DNS/Utilities
Requires:       %{NAME}-chroot
Provides:       dns_daemon
Requires:bind-license = %{version}-%{release}

%description lwresd
Bind-lwresd provides resolution services to local clients using a
combination of the lightweight resolver library liblwres and the
resolver daemon process lwresd running on the local host.  These
communicate using a simple UDP-based protocol, the "lightweight
resolver protocol" that is distinct from and simpler than the full DNS
protocol.

%package utils
Summary:        Utilities to query and test DNS
Group:          Productivity/Networking/DNS/Utilities
Provides:       bind9-utils
Provides:       bindutil
Provides:       dns_utils
Obsoletes:      bind9-utils
Obsoletes:      bindutil
Requires:bind-license = %{version}-%{release}

%description utils
This package includes the utilities host, dig, and nslookup used to
test and query the Domain Name System (DNS).  The Berkeley Internet
Name Domain (BIND) DNS server is found in the package named bind.

%package chroot
Summary:        A chroot runtime environment for the ISC BIND DNS server, named(8)
Group:          System Environment/Daemons
Prefix:         %{chroot_prefix}
Requires(post): grep
Requires(preun):grep
Requires:       bind = %{version}-%{release}
Requires:bind-license = %{version}-%{release}

%description chroot
This package contains a tree of files which can be used as a
chroot(2) jail for the named(8) program from the BIND package.
Based on the code from Jan "Yenya" Kasprzak <kas@fi.muni.cz>


%prep
%setup -q  -n %{NAME}-%{VER}


# ---------------------------------------------------------------------------

# Common patches
#%patch5 -p1 -b .nonexec
%patch10 -p1 -b .PIE
%patch16 -p1 -b .redhat_doc
#%patch104 -p1 -b .dyndb
#%patch117 -p1 -b .rh725741
%if %{SDB}
%patch101 -p1 -b .old-api
mkdir bin/named-sdb
cp -r bin/named/* bin/named-sdb
%patch11 -p1 -b .sdbsrc
# SDB ldap
cp -fp contrib/sdb/ldap/ldapdb.[ch] bin/named-sdb
# SDB postgreSQL
cp -fp contrib/sdb/pgsql/pgsqldb.[ch] bin/named-sdb
# SDB sqlite
cp -fp contrib/sdb/sqlite/sqlitedb.[ch] bin/named-sdb
#
# SDB Berkeley DB -  RH enable Berkeley DB DLZ backend (#804478)
cp -fp contrib/sdb/bdb/bdb.[ch] bin/named-sdb
#
# SDB dir
cp -fp contrib/sdb/dir/dirdb.[ch] bin/named-sdb
# SDB tools
mkdir -p bin/sdb_tools
cp -fp %{SOURCE30} bin/sdb_tools/ldap2zone.c
cp -fp %{SOURCE7} bin/sdb_tools/Makefile.in
#cp -fp contrib/sdb/bdb/zone2bdb.c bin/sdb_tools
cp -fp contrib/sdb/ldap/{zone2ldap.1,zone2ldap.c} bin/sdb_tools
cp -fp contrib/sdb/pgsql/zonetodb.c bin/sdb_tools
cp -fp contrib/sdb/sqlite/zone2sqlite.c bin/sdb_tools
%patch12 -p1 -b .sdb
%endif
%if %{SDB}
%patch17 -p1 -b .fix_sdb_ldap
%endif
%if %{SDB}
%patch62 -p1 -b .sdb-sqlite-bld
%endif
%patch87 -p1 -b .parallel

# XXX due new libtool. Not sure about proper upstream approach yet.
mkdir m4

%patch102 -p1 -b .rh452060
%patch106 -p0 -b .rh490837
%patch107 -p1 -b .dist-pkcs11
%patch109 -p1 -b .rh478718
%patch111 -p1 -b .exportlib
%patch112 -p1 -b .rh645544
%patch118 -p1 -b .rh699951
%patch119 -p1 -b .rh693982
%patch122 -p1 -b .dlz_buildfix
%patch123 -p1 -b .rh735103

# Sparc and s390 arches need to use -fPIE
%ifarch sparcv9 sparc64 s390 s390x
for i in bin/named{,-sdb}/{,unix}/Makefile.in; do
        sed -i 's|fpie|fPIE|g' $i
done
%endif
:;

# ---------------------------------------------------------------------------
%build

export CPPFLAGS="$CPPFLAGS -DDIG_SIGCHASE"
export STD_CDEFINES="$CPPFLAGS" CC=gcc
##export CFLAGS="$CFLAGS $RPM_OPT_FLAGS -fno-strict-aliasing" LDFLAGS="-L%{_libdir} -R/usr/lib -lidn -lidn2"
export CFLAGS="$RPM_OPT_FLAGS -DNO_VERSION_DATE -fno-strict-aliasing -fpie $(getconf LFS_CFLAGS)" LDFLAGS="-L%{_libdir} -L/usr/lib64/mysql -pie"

sed -i -e \
's/RELEASEVER=\(.*\)/RELEASEVER=\1-Remsnet_LTD-%{version}-%{release}/' \
version

libtoolize -c -f
aclocal  -I m4 --force
autoconf -f


%configure \
        --prefix=%{_prefix} \
        --bindir=%{_bindir} \
        --sbindir=%{_sbindir} \
        --sharedstatedir=/var/lib \
        --libexecdir=/usr/libexec \
        --localstatedir=%{_var} \
        --includedir=%{_includedir}/bind9 \
        --libdir=%{_libdir} \
        --datadir=%{_datadir} \
        --mandir=%{_datadir}/man \
        --infodir=%{_datadir}/info \
        --docdir=%{_datadir}/doc \
        --sysconfdir=%{_sysconfdir} \
        --host=x86_64-redhat-linux-gnu \
        --target=x86_64-redhat-linux-gnu \
        --with-docbook-xsl=/usr/share/sgml/docbook/xsl-stylesheets \
        --enable-newstats \
        --disable-static \
        --enable-exportlib \
        --with-export-libdir=%{_libdir} \
        --with-export-includedir=%{_includedir} \
        --with-openssl \
        --enable-threads \
        --disable-openssl-version-check \
        --with-libtool \
        --with-pic \
        --with-python \
%if %{PKCS11}
        --with-pkcs11=%{_libdir}/pkcs11/p11-kit-trust.so \
%endif
%if %{SDB}
        --with-dlopen=yes \
        --with-dlz-ldap=yes \
        --with-dlz-postgres=yes \
        --with-dlz-filesystem=yes \
        --with-dlz-bdb=yes \
%endif
%if %{MYSQLDB}
        --with-dlz-mysql=yes \
%endif
%if %{BDB}
        --with-dlz-bdb=yes \
%endif
%if %{GSSTSIG}
        --with-gssapi=yes \
%endif
%if %{SPNEGO}
        --disable-isc-spnego \
%endif
%if %{IDN}
        --with-idnlib='-L/usr/lib -R/usr/lib -lidn -lidn2' \
%endif
        --with-libxml2 \
        --enable-filter-aaaa \
        --enable-rrl \
        --with-ecdsa \
        --enable-fixed-rrset

%{__make} %{?_smp_mflags}

#--with-dlz-bdb='-L/usr/lib -R/usr/lib -ldb -ldb4' \
# ---------------------------------------------------------------------------
# Regenerate dig.1 manpage
pushd bin/dig
make man
popd
pushd bin/nsupdate
make man
popd
pushd doc/arm
make Bv9ARM.html
popd

# Remove this backup file to avoid be picked by %%doc directive
rm -f doc/arm/Bv9ARM-book.xml.rh873624

# ---------------------------------------------------------------------------
%if %{test}
%check
if [ "`whoami`" = 'root' ]; then
  set -e
  chmod -R a+rwX .
  pushd bin/tests
  pushd system
  ./ifconfig.sh up
  popd
  make test
  e=$?
  pushd system
  ./ifconfig.sh down
  popd
  popd
  if [ "$e" -ne 0 ]; then
    echo "ERROR: this build of BIND failed 'make test'. Aborting."
    exit $e;
  fi;
else
  echo 'only root can run the tests (they require an ifconfig).'
%endif

# ---------------------------------------------------------------------------

# modify settings of some files regarding to OS version and vendor
function replaceStrings()
{
file="$1"
sed -e "s@__NSD__@/lib@g" \
        -e "s@__BIND_PACKAGE_NAME__@%{pkg_name}@g" \
        -e "s@__VENDOR__@%{VENDOR}@g" \
        "${file}" >"${file}.new" && \
                mv "${file}.new" "${file}"

}
# ---------------------------------------------------------------------------
%install
rm -rf ${RPM_BUILD_ROOT}


cp  --preserve=timestamps %{SOURCE5} doc/rfc

# Build directory hierarchy
mkdir -p ${RPM_BUILD_ROOT}/etc/{rc.d/init.d,logrotate.d,NetworkManager/dispatcher.d,slp.reg.d,openldap/schema}
mkdir -p ${RPM_BUILD_ROOT}/etc/portreserve
mkdir -p ${RPM_BUILD_ROOT}/usr/lib64/bind
mkdir -p ${RPM_BUILD_ROOT}/usr/lib/bind9
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/{dst,irs,isc,dns,isccfg}
mkdir -p ${RPM_BUILD_ROOT}%{_includedir}/bind9/{dst,irs,isc,dns,isccfg}
mkdir -p ${RPM_BUILD_ROOT}/var/named/{etc,slaves,master,data,dynamic}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/{man1,man3,man5,man8}
mkdir -p ${RPM_BUILD_ROOT}/var/run/named
mkdir -p ${RPM_BUILD_ROOT}/var/log
mkdir -p ${RPM_BUILD_ROOT}/var/adm/fillup-templates
mkdir -p  ${RPM_BUILD_ROOT}/usr/{bin,%{_lib},sbin,include,share/man,share/doc/%{name},share/info,lib64}

#chroot
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/{dev,etc/named,var}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/var/{log,named,run/named,tmp}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/etc/{pki/dnssec-keys,named}
mkdir -p ${RPM_BUILD_ROOT}/%{chroot_prefix}/usr/lib64
mkdir -p ${RPM_BUILD_ROOT}/var/named/chroot/var/named

# these are required to prevent them being erased during upgrade of previous
# versions that included them (bug #130121):
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/null
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/random
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/dev/zero
touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/etc/localtime

touch ${RPM_BUILD_ROOT}/%{chroot_prefix}/etc/named.conf
#end chroot

# main install
make DESTDIR=${RPM_BUILD_ROOT} install

# Remove unwanted files
rm -f ${RPM_BUILD_ROOT}/etc/bind.keys

install -m 755 %SOURCE2 ${RPM_BUILD_ROOT}/etc/rc.d/init.d/named
install -m 644 %SOURCE3 ${RPM_BUILD_ROOT}/etc/logrotate.d/named
install -m 755 %SOURCE4 ${RPM_BUILD_ROOT}/etc/NetworkManager/dispatcher.d/13-named
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig
install -m 644 %{SOURCE1} ${RPM_BUILD_ROOT}%{_sysconfdir}/sysconfig/named

%if %{SDB}
mkdir -p ${RPM_BUILD_ROOT}/etc/openldap/schema
install -m 644 %{SOURCE8} ${RPM_BUILD_ROOT}/etc/openldap/schema/dnszone.schema
install -m 644 %{SOURCE12} contrib/sdb/pgsql/
#
# SDB manpages
install -m 644 %{SOURCE31} ${RPM_BUILD_ROOT}%{_mandir}/man1/ldap2zone.1
install -m 644 %{SOURCE32} ${RPM_BUILD_ROOT}%{_mandir}/man8/named-sdb.8
install -m 644 %{SOURCE33} ${RPM_BUILD_ROOT}%{_mandir}/man1/zonetodb.1
install -m 644 %{SOURCE34} ${RPM_BUILD_ROOT}%{_mandir}/man1/zone2sqlite.1
%endif

install -m 644 %{SOURCE31} ${RPM_BUILD_ROOT}%{_sysconfdir}/portreserve/named

# Files required to run test-suite outside of build tree:
install -m 644 config.h ${RPM_BUILD_ROOT}/%{_includedir}/bind9/
install -m 644 lib/dns/include/dns/forward.h ${RPM_BUILD_ROOT}/%{_includedir}/bind9/dns/
install -m 644 lib/isc/unix/include/isc/keyboard.h ${RPM_BUILD_ROOT}/%{_includedir}/bind9/isc/

# Remove libtool .la files:
##find ${RPM_BUILD_ROOT}/%{_libdir} -name '*.la' -exec '/bin/rm' '-f' '{}' ';';
# /usr/lib/rpm/brp-compress
#

# Ghost config files:
touch ${RPM_BUILD_ROOT}%{_localstatedir}/log/named.log

# copy sample  configuration files from prepared sample bind9-config.tar.bz2 ( Source28 )
mkdir -p sample
tar -C ${RPM_BUILD_ROOT} -xpfj %{SOURCE28} -C sample

test -d  ${RPM_BUILD_ROOT}/etc/named || mkdir ${RPM_BUILD_ROOT}/etc/named
install -m 644  ${RPM_BUILD_ROOT}

install -m 644 bind.keys ${RPM_BUILD_ROOT}/etc/named.iscdlv.key
install -m 644 %{SOURCE36} ${RPM_BUILD_ROOT}/etc/trusted-key.key

install -m 644 %{SOURCE5}  ./rfc1912.txt
install -m 644 %{SOURCE21} ./Copyright

# sample bind configuration files for %%doc:
mkdir -p sample/etc sample/var/named/{data,slaves}
#
# Copy default sample config - caching named
install -m 644 ${RPM_BUILD_ROOT}/var/named/{named.ca,named.localhost,named.loopback,named.empty}  sample/var/named
install -m 644 sample/etc/named.rfc1912.zones ${RPM_BUILD_ROOT}/var/named/named.rfc1912.zones
install -m 644 sample/etc/named.conf ${RPM_BUILD_ROOT}/etc/named.conf
install -m 644 sample/etc/named.root.key ${RPM_BUILD_ROOT}/etc/named.root.key
install -m 644 sample/etc/rndc.conf ${RPM_BUILD_ROOT}/etc/rndc.conf
touch ${RPM_BUILD_ROOT}/etc/rndc.key
install -m 644 sample/named/named.ca ${RPM_BUILD_ROOT}/var/named/named.ca
install -m 644 sample/named/named.empty ${RPM_BUILD_ROOT}/var/named/named.empty

for f in my.internal.zone.db slaves/my.slave.internal.zone.db slaves/my.ddns.internal.zone.db my.external.zone.db; do
  echo '@ in soa localhost. root 1 3H 15M 1W 1D
  ns localhost.' > sample/var/named/$f;
done
:;


# ---------------------------------------------------------------------------
%pre
if [ "$1" -eq 1 ]; then
/usr/bin/getent group named >/dev/null 2>&1 || %{GROUPADD_NAMED} >/dev/null 2>&1
/usr/bin/getent passwd named >/dev/null 2>&1 || %{USERADD_NAMED} >/dev/null 2>&1
fi
:;


%post
/sbin/ldconfig
/sbin/chkconfig --add named
if [ "$1" -eq 1 ]; then
  [ -x /sbin/restorecon ] && /sbin/restorecon /etc/rndc.* /etc/named.* >/dev/null 2>&1 ;
  # rndc.key has to have correct perms and ownership, CVE-2007-6283
  [ -e /etc/rndc.key ] && chown root:named /etc/rndc.key
  [ -e /etc/rndc.key ] && chmod 0640 /etc/rndc.key
fi
:;

%preun
if [ "$1" -eq 0 ]; then
  /sbin/service named stop >/dev/null 2>&1 || :;
  /sbin/chkconfig --del named || :;
fi;
:;

%postun
/sbin/ldconfig
if [ "$1" -ge 1 ]; then
  /sbin/service named try-restart >/dev/null 2>&1 || :;
fi;
:;

# ---------------------------------------------------------------------------

%if %{SDB}
%post sdb
/sbin/service named try-restart > /dev/null 2>&1 || :;

%postun sdb
/sbin/service named try-restart > /dev/null 2>&1 || :;
%endif


# ---------------------------------------------------------------------------
%pre lwresd
/usr/bin/getent group named >/dev/null 2>&1 || %{GROUPADD_NAMED}
/usr/bin/getent passwd named >/dev/null 2>&1 || %{USERADD_NAMED}

test -x /etc/init.d/lwresd && /sbin/chkconfig --add lwresd > /dev/null 2>&1
test -x /etc/init.d/lwresd && /sbin/chkconfig lwresd on > /dev/null 2>&1

%post lwresd
# Create a key if /usr/sbin/rndc-confgen is installed.
if [ -x /usr/sbin/rndc-confgen -a ! -f /etc/rndc.key ]; then
        /usr/sbin/rndc-confgen -a -b 512 -r /dev/urandom
        chmod 0640 /etc/rndc.key
        chown root:named /etc/rndc.key
fi
# delete an emtpy lwresd.conf file
if [ ! -s /etc/lwresd.conf ]; then
    rm -f /etc/lwresd.conf
fi
#
/sbin/service lwresd try-restart > /dev/null 2>&1


%preun lwresd
/sbin/service lwresd stop > /dev/null 2>&1
/sbin/chkconfig lwresd off > /dev/null 2>&1
pkill -9 lwresd > /dev/null 2>&1


%postun lwresd
/sbin/chkconfig --del lwresd > /dev/null 2>&1

# ---------------------------------------------------------------------------
%post utils
/sbin/ldconfig
# Create a key if lwresd is installed.
if [ -x usr/sbin/lwresd -a ! -f etc/rndc.key ]; then
        usr/sbin/rndc-confgen -a -b 512 -r dev/urandom
        chmod 0640 etc/rndc.key
        chown root:named etc/rndc.key
fi
# ---------------------------------------------------------------------------

%post libs
/sbin/ldconfig -l || exit 1

%postun libs
/sbin/ldconfig -l || exit 1

# ---------------------------------------------------------------------------
# Automatically update configuration from "dnssec-conf-based" to "BIND-based"
%triggerpostun -n bind -- dnssec-conf
[ -r '/etc/named.conf' ] || exit 0
cp -fp /etc/named.conf /etc/named.conf.rpmsave
if grep -Eq '/etc/(named.dnssec.keys|pki/dnssec-keys)' /etc/named.conf; then
  if grep -q 'dlv.isc.org.conf' /etc/named.conf; then
    # DLV is configured, reconfigure it to new configuration
    sed -i -e 's/.*dnssec-lookaside.*dlv\.isc\.org\..*/dnssec-lookaside auto;\
bindkeys-file "\/etc\/named.iscdlv.key";/' /etc/named.conf
  fi
  sed -i -e '/.*named\.dnssec\.keys.*/d' -e '/.*pki\/dnssec-keys.*/d' \
    /etc/named.conf
  /sbin/service named try-restart > /dev/null 2>&1 || :;
fi

# ---------------------------------------------------------------------------
%post chroot
if [ "$1" -gt 0 ]; then
  [ -e %{chroot_prefix}/dev/random ] || \
    /bin/mknod %{chroot_prefix}/dev/random c 1 8
  [ -e %{chroot_prefix}/dev/zero ] || \
    /bin/mknod %{chroot_prefix}/dev/zero c 1 5
  [ -e %{chroot_prefix}/dev/null ] || \
    /bin/mknod %{chroot_prefix}/dev/null c 1 3
  rm -f %{chroot_prefix}/etc/localtime
  cp /etc/localtime %{chroot_prefix}/etc/localtime

test -f /etc/sysconfig/named || touch /etc/sysconfig/named
  if ! grep -q '^ROOTDIR=' /etc/sysconfig/named; then
    echo 'ROOTDIR=/var/named/chroot' >> /etc/sysconfig/named
    /sbin/service named try-restart > /dev/null 2>&1 || :;
  fi

fi;
:;

%posttrans chroot
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
  [ -x /sbin/restorecon ] && /sbin/restorecon %{chroot_prefix}/dev/* > /dev/null 2>&1;
fi;
:;

%preun chroot
if [ "$1" -eq 0 ]; then
  rm -f %{chroot_prefix}/dev/{random,zero,null}
  rm -f %{chroot_prefix}/etc/localtime
#
test -f /etc/sysconfig/named || touch /etc/sysconfig/named
  if grep -q '^ROOTDIR=' /etc/sysconfig/named; then
    # NOTE: Do NOT call `service named try-restart` because chroot
    # files will remain mounted.
    START=no
    [ -e /var/lock/subsys/named ] && START=yes
    /sbin/service named stop > /dev/null 2>&1 || :;
    sed -i -e '/^ROOTDIR=.*/d' /etc/sysconfig/named
    if [ "x$START" = xyes ]; then
      /sbin/service named start > /dev/null 2>&1 || :;
    fi
  fi
fi
:;

# ---------------------------------------------------------------------------
%files
%defattr(-,root,root,-)
%dir %{_libdir}/bind
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/sysconfig/named
%config(noreplace) %attr(-,root,named) %{_sysconfdir}/named.iscdlv.key
%config(noreplace) %attr(-,root,named) %{_sysconfdir}/named.root.key
%{_sysconfdir}/rc.d/init.d/named
%{_sysconfdir}/NetworkManager/dispatcher.d/13-named
%{_sysconfdir}/portreserve/named
%{_sbindir}/arpaname
%{_sbindir}/ddns-confgen
%{_sbindir}/genrandom
%{_sbindir}/named-journalprint
%{_sbindir}/nsec3hash
%{_sbindir}/dnssec*
%{_sbindir}/named-check*
%{_sbindir}/named
%{_sbindir}/rndc*
%{_sbindir}/named-compilezone
%{_sbindir}/isc-hmac-fixup
%{_bindir}/bind9-config

# Hide configuration
%defattr(0640,root,named,0750)
%dir %{_sysconfdir}/named
%dir %{_localstatedir}/named
%config(noreplace) %verify(not link) %{_sysconfdir}/named.conf
%config(noreplace) %verify(not link) %{_sysconfdir}/named.rfc1912.zones
%config %verify(not link) %{_localstatedir}/named/named.ca
%config %verify(not link) %{_localstatedir}/named/named.localhost
%config %verify(not link) %{_localstatedir}/named/named.loopback
%config %verify(not link) %{_localstatedir}/named/named.empty
%defattr(0660,named,named,0770)
%dir %{_localstatedir}/named/slaves
%dir %{_localstatedir}/named/data
%dir %{_localstatedir}/named/dynamic
%ghost %{_localstatedir}/log/named.log
%defattr(0640,root,named,0750)
%ghost %config(noreplace) %{_sysconfdir}/rndc.key
# ^- rndc.key now created on first install only if it does not exist
# %verify(not size,not md5) %config(noreplace) %attr(0640,root,named) /etc/rndc.conf
# ^- Let the named internal default rndc.conf be used -
#    rndc.conf not required unless it differs from default.
%ghost %config(noreplace) %{_sysconfdir}/rndc.conf
# ^- The default rndc.conf which uses rndc.key is in named's default internal config -
#    so rndc.conf is not necessary.
%config(noreplace) %{_sysconfdir}/logrotate.d/named
%defattr(-,named,named,-)
%dir %{_localstatedir}/run/named


%files libs
%defattr(-,root,root,-)
%{_libdir}/libbind9.so
%{_libdir}/libbind9.so.*
%{_libdir}/libdns.so
%{_libdir}/libdns.so.*
%{_libdir}/libisc.so
%{_libdir}/libisc.so.*
%{_libdir}/libisccc.so
%{_libdir}/libisccc.so.*
%{_libdir}/libisccfg.so
%{_libdir}/libisccfg.so.*
%{_libdir}/liblwres.so
%{_libdir}/liblwres.so.*
%{_libdir}/liblwres.so.91
%{_libdir}/liblwres.so.91.0.0

%exclude %{_libdir}/libdns-export.*
%exclude %{_libdir}/libirs-export.*
%exclude %{_libdir}/libisc-export.*
%exclude %{_libdir}/libisccfg-export.*

%files libs-lite
%defattr(-,root,root,-)
%{_libdir}/libdns-export.*
%{_libdir}/libirs-export.*
%{_libdir}/libisc-export.*
%{_libdir}/libisccfg-export.*

%files lwresd
%defattr(-,root,root)
%{_sbindir}/lwresd


%files utils
%defattr(-,root,root,-)
%{_bindir}/dig
%{_bindir}/host
%{_bindir}/nslookup
%{_bindir}/nsupdate
%{_bindir}/bind9-config
%{_sysconfdir}/trusted-key.key


%if %{SDB}
%files sdb
%defattr(-,root,root,-)
%{_mandir}/man1/zone2ldap.1*
%{_mandir}/man1/ldap2zone.1*
%{_mandir}/man1/zonetodb.1*
%{_mandir}/man1/zone2sqlite.1*
%{_mandir}/man8/named-sdb.8*
%doc contrib/sdb/ldap/README.ldap contrib/sdb/ldap/INSTALL.ldap contrib/sdb/pgsql/README.sdb_pgsql
%dir %{_sysconfdir}/openldap/schema
%config(noreplace) %{_sysconfdir}/openldap/schema/dnszone.schema
%{_sbindir}/named-sdb
%{_sbindir}/zone2ldap
%{_sbindir}/ldap2zone
%{_sbindir}/zonetodb
%{_sbindir}/zone2sqlite
%endif


%if %{DEVEL}
%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/bind9
%{_includedir}/bind9/*
%{_bindir}/isc-config.sh
%{_libdir}/*.la
%endif

%files lite-devel
%defattr(-,root,root,-)
%{_includedir}/dns
%{_includedir}/dst
%{_includedir}/irs
%{_includedir}/isc
%{_includedir}/isccfg


%if %{PKCS11}
%files pkcs11
%defattr(-,root,root,-)
%{_sbindir}/pkcs11-destroy
%{_sbindir}/pkcs11-keygen
%{_sbindir}/pkcs11-list
%endif

%files license
%defattr(-,root,root,-)
%doc COPYRIGHT

%files doc
%defattr(-,root,root,-)
#%doc %{_datadir}/doc/%{name}-*

%doc %{_mandir}/man1/arpaname.1.gz
%doc %{_mandir}/man1/isc-config.sh.1.gz
%doc %{_mandir}/man1/host.1*
%doc %{_mandir}/man1/nsupdate.1*
%doc %{_mandir}/man1/dig.1*
%doc %{_mandir}/man1/nslookup.1*
%doc %{_mandir}/man1/bind9-config.1*

%doc %{_mandir}/man3/*
%doc %{_mandir}/man5/rndc.conf.5.gz
%doc %{_mandir}/man5/named.conf.5.gz

%doc %{_mandir}/man8/named-checkconf.8.gz
%doc %{_mandir}/man8/named-checkzone.8.gz
%doc %{_mandir}/man8/named.8.gz
%doc %{_mandir}/man8/named-compilezone.8.gz

%doc %{_mandir}/man8/lwresd.8.gz
%doc %{_mandir}/man8/ddns-confgen.8.gz
%doc %{_mandir}/man8/dnssec-checkds.8.gz
%doc %{_mandir}/man8/dnssec-coverage.8.gz
%doc %{_mandir}/man8/dnssec-dsfromkey.8.gz
%doc %{_mandir}/man8/dnssec-keyfromlabel.8.gz
%doc %{_mandir}/man8/dnssec-keygen.8.gz
%doc %{_mandir}/man8/dnssec-revoke.8.gz
%doc %{_mandir}/man8/dnssec-settime.8.gz
%doc %{_mandir}/man8/dnssec-signzone.8.gz
%doc %{_mandir}/man8/dnssec-verify.8.gz
%doc %{_mandir}/man8/genrandom.8.gz
%doc %{_mandir}/man8/isc-hmac-fixup.8.gz
%doc %{_mandir}/man8/named-journalprint.8.gz
%doc %{_mandir}/man8/nsec3hash.8.gz
%doc %{_mandir}/man8/rndc.8.gz
%doc %{_mandir}/man8/rndc-confgen.8.gz
%doc %{_mandir}/man8/dnssec-importkey.8.gz

%if %{PKCS11}
%doc %{_mandir}/man8/pkcs11-list.8.gz
%doc %{_mandir}/man8/pkcs11-keygen.8.gz
%doc %{_mandir}/man8/pkcs11-destroy.8.gz
%endif


%files chroot
/var/named/chroot/dev/null
/var/named/chroot/dev/random
/var/named/chroot/dev/zero
/var/named/chroot/etc/localtime
/var/named/chroot/etc/named.conf



%clean
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}
[ -d $RPM_BUILD_DIR/%{name}-%{version} ] && rm -rf $RPM_BUILD_DIR/%{name}-%{version}


%changelog
* Sun Nov  9 2014 Horst venzke - support@remsnet.de -r  9.9.5-P1
 - BIND DLZ for centos 6.5

* Fri Apr 4 2014 Horst venzke - support@remsnet.de -r 9.9.4-P1
 - BIND DLZ for opensuse 13.1
