Summary:	Extremely simple MTA to get mail off the system to a mail hub
Name:		ssmtp
Version:	2.60.3
Release:	0.1
License:	GPL
Group:		Networking/Daemons
Source0:	%{name}_%{version}.tar.gz
#Source0-md5:	b9b1c07f513ff2b46ae8a09eaf3e04e5
Patch0:		%{name}-nonsl.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A secure, effective and simple way of getting mail off a system to
your mail hub. It contains no suid-binaries or other dangerous things
- no mail spool to poke around in, and no daemons running in the
background. Mail is simply forwarded to the configured mailhost.
Extremely easy configuration. WARNING: the above is all it does; it
does not receive mail, expand aliases or manage a queue. That belongs
on a mail hub with a system administrator.

%prep
%setup -q -n %{name}-2.60
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure
%{__make} SSMTPCONFDIR=/etc/ssmtp

%install
rm -rf $RPM_BUILD_ROOT

install -D ssmtp $RPM_BUILD_ROOT/%{_sbindir}/ssmtp
install -D ssmtp.8 $RPM_BUILD_ROOT/%{_mandir}/man8/ssmtp.8
install -D ssmtp.conf $RPM_BUILD_ROOT%{_sysconfdir}/ssmtp/ssmtp.conf
install revaliases $RPM_BUILD_ROOT%{_sysconfdir}/ssmtp/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TLS
%attr(755,root,root) %{_sbindir}/*
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ssmtp/ssmtp.conf
%attr( 644,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ssmtp/revaliases

%{_mandir}/man8/ssmtp*
