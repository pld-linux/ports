#
# TODO:
# Sumamry, Desription,
#
# Attention - package are in development !
#
%define		snap 020412
Summary:	ports
Summary(pl):	ports
Name:		ports
Version:	%{snap}
Release:	0.1
License:	GPL
Group:		Applications/Archving
######		Unknown group!
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-PLD.patch
URL:		http://www.nuulinux.org/
Requires:	/bin/sh
Requires:	links
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ports for Linux

%description -l pl

%prep
%setup -q -n %{name}
%patch -p0

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT/%{_bindir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}
cp -r * $RPM_BUILD_ROOT%{_datadir}/%{name}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/internals/ports $RPM_BUILD_ROOT%{_sysconfdir}
mv $RPM_BUILD_ROOT%{_datadir}/%{name}/internals/pkg_ports $RPM_BUILD_ROOT/%{_bindir}
rm -rf $(find $RPM_BUILD_ROOT -name CVS)
rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/internals/install.sh

gzip -9nf internals/doc/{README,INSTALL,TODO,install-lists}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc internals/doc/*.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_sysconfdir}