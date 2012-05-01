%define glib2_version		2.22
%define dbus_version		1.2
%define dbus_glib_version	0.86
%define net_snmp_version	5.5

Name:		foghorn
Version:	0.1.2
Release:	1%{?dist}
Summary:	Foghorn DBUS/SNMP service

Group:		System Environment/Base
License:	GPLv2+
URL:		https://fedorahosted.org/foghorn
Source0:	http://people.redhat.com/~rohara/foghorn/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	autoconf
BuildRequires:	automake

BuildRequires:	glib2-devel >= %{glib2_version}
BuildRequires:	dbus-devel >= %{dbus_version}
BuildRequires:	dbus-glib-devel >= %{dbus_glib_version}
BuildRequires:	net-snmp-devel >= %{net_snmp_version}

Requires:	glib2 >= %{glib_version}
Requires:	dbus >= %{dbus_version}
Requires:	dbus-glib >= %{dbus_glib_version}
Requires:	net-snmp >= %{net_snmp_version}
Requires:       cluster-snmp
Requires:	initscripts

ExclusiveArch:	i686 x86_64

%description
Foghorn listens for specific DBUS signals and translates those signals to SNMP traps.

%prep
%setup -q

%build
autoreconf
%configure --prefix=/usr
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README AUTHORS NEWS COPYING
%{_sbindir}/foghorn
%attr(0755, root, root) %{_initrddir}/foghorn
%{_datadir}/snmp/mibs/REDHAT-FENCE-MIB
%{_datadir}/snmp/mibs/REDHAT-FOGHORN-MIB
%{_datadir}/snmp/mibs/REDHAT-RGMANAGER-MIB
%{_sysconfdir}/dbus-1/system.d/dbus-foghorn.conf
%{_mandir}/man8/foghorn*

%changelog
* Fri Feb 4 2011 Ryan O'Hara <rohara@redhat.com> - 0.1.2-1
- Add foghorn man page.
- Rebase to upstream version 0.1.2.
- Resolves: rhbz#660324

* Fri Jan 15 2011 Ryan O'Hara <rohara@redhat.com> - 0.1.1-2
- Add requires initscripts to spec file.
- Resolves: rhbz#660324

* Fri Jan 14 2011 Ryan O'Hara <rohara@redhat.com> - 0.1.1-1
- Rebase to 0.1.1 from upstream to resolve build issues.
- Resolves: rhbz#660324

* Thu Jan 13 2011 Ryan O'Hara <rohara@redhat.com> - 0.1-1
- Initial release.
