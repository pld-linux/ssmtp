Summary:	Extremely simple MTA to get mail off the system to a mail hub
Summary(pl):	Skrajnie prosty MTA do przekazywania poczty z systemu do huba
Name:		ssmtp
Version:	2.60.3
Release:	0.3
License:	GPL
Group:		Networking/Daemons
Source0:	%{name}_%{version}.tar.gz
#Source0-md5:	b9b1c07f513ff2b46ae8a09eaf3e04e5
Patch0:		%{name}-nonsl.patch
BuildRequires:	autoconf
BuildRequires:	automake
Provides:	smtpdaemon
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	smtpdaemon

%description
A secure, effective and simple way of getting mail off a system to
your mail hub. It contains no suid-binaries or other dangerous things
- no mail spool to poke around in, and no daemons running in the
background. Mail is simply forwarded to the configured mailhost.
Extremely easy configuration. WARNING: the above is all it does; it
does not receive mail, expand aliases or manage a queue. That belongs
on a mail hub with a system administrator.

%description -l pl
Bezpieczny, efektywny i prosty sposób przekazywania poczty z systemu
do w³asnego huba pocztowego. Nie zawiera suidowych binarek ani innych
niebezpiecznych rzeczy - nie ma spoola do wpychania czegokolwiek ani
demonów dzia³aj±cych w tle. Poczta jest po prostu przekazywana do
zewnêtrznego, skonfigurowanego serwera pocztowego. Skrajnie prosta
konfiguracja. UWAGA: powy¿sze to wszystko, co robi ten program; nie
odbiera poczty, nie rozwija aliasów ani nie zarz±dza kolejk±. To
nale¿y do huba pocztowego z w³asnym administratorem.

%prep
%setup -q -n %{name}-2.60
%patch0 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure

%{__make} \
	SSMTPCONFDIR=/etc/mail

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/mail,%{_libdir}}

install ssmtp $RPM_BUILD_ROOT%{_sbindir}/ssmtp
install ssmtp.8 $RPM_BUILD_ROOT%{_mandir}/man8/ssmtp.8
install ssmtp.conf revaliases $RPM_BUILD_ROOT%{_sysconfdir}/mail
ln -sf %{_sbindir}/ssmtp $RPM_BUILD_ROOT%{_libdir}/sendmail
ln -sf ssmtp $RPM_BUILD_ROOT%{_sbindir}/sendmail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TLS
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_libdir}/sendmail
%dir %{_sysconfdir}/mail
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mail/ssmtp.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mail/revaliases
%{_mandir}/man8/ssmtp*
