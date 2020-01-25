# TODO:
# - split like https://build.opensuse.org/package/view_file/home:guillomovitch/fusioninventory-agent/fusioninventory-agent.spec
# - add cron jobs
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	FusionInventory
%define		pnam	Agent
Summary:	FusionInventory agent
Name:		FusionInventory-Agent
Version:	2.3.19
Release:	0.1
License:	GPL
Group:		Applications/System
Source0:	http://www.cpan.org/modules/by-authors/id/G/GB/GBOUGARD/%{name}-%{version}.tar.gz
# Source0-md5:	649aeefe3cb7140f60d582e3c6008f97
URL:		http://fusioninventory.org/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(HTTP::Proxy)
BuildRequires:	perl(HTTP::Server::Simple::Authen)
BuildRequires:	perl(IO::Capture::Stderr)
BuildRequires:	perl(Parallel::ForkManager)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(XML::TreePP) >= 0.26
BuildRequires:	perl-File-Which
BuildRequires:	perl-HTTP-Server-Simple
BuildRequires:	perl-IO-Socket-SSL
BuildRequires:	perl-IPC-Run
BuildRequires:	perl-LWP-Protocol-https
BuildRequires:	perl-Net-IP
BuildRequires:	perl-Net-SNMP
BuildRequires:	perl-Test-Deep
BuildRequires:	perl-Test-Exception
BuildRequires:	perl-Test-MockModule
BuildRequires:	perl-Test-MockObject
BuildRequires:	perl-Test-NoWarnings
BuildRequires:	perl-Text-Template
BuildRequires:	perl-UNIVERSAL-require
BuildRequires:	perl-libwww >= 5.8
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The FusionInventory Agent is a generic multi-platform agent. It can
perform a large array of management tasks, such as local inventory,
software deployment or network discovery. It can be used either
standalone, or in combination with a compatible server (OCS Inventory,
GLPI, OTRS, Uranos, …) acting as a centralized control point.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	PREFIX=%{_prefix} \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes doc README
%attr(755,root,root) %{_bindir}/fusioninventory-agent
%attr(755,root,root) %{_bindir}/fusioninventory-esx
%attr(755,root,root) %{_bindir}/fusioninventory-injector
%attr(755,root,root) %{_bindir}/fusioninventory-inventory
%attr(755,root,root) %{_bindir}/fusioninventory-netdiscovery
%attr(755,root,root) %{_bindir}/fusioninventory-netinventory
%attr(755,root,root) %{_bindir}/fusioninventory-wakeonlan
%{_datadir}/fusioninventory
%{_mandir}/man1/fusioninventory-agent.1*
%{_mandir}/man1/fusioninventory-esx.1*
%{_mandir}/man1/fusioninventory-injector.1*
%{_mandir}/man1/fusioninventory-inventory.1*
%{_mandir}/man1/fusioninventory-netdiscovery.1*
%{_mandir}/man1/fusioninventory-netinventory.1*
%{_mandir}/man1/fusioninventory-wakeonlan.1*
