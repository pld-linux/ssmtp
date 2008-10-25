Summary:	Extremely simple MTA to get mail off the system to a mail hub
Summary(pl.UTF-8):	Skrajnie prosty MTA do przekazywania poczty z systemu do huba
Name:		ssmtp
Version:	2.62
Release:	2
License:	GPL
Group:		Networking/Daemons/SMTP
Source0:	http://http.us.debian.org/debian/pool/main/s/ssmtp/%{name}_%{version}.orig.tar.gz
# Source0-md5:	257ac04e62ab7e3616e220333a1140cb
Patch0:		%{name}-nonsl.patch
BuildRequires:	autoconf
BuildRequires:	automake
Provides:	smtpdaemon
Obsoletes:	courier
Obsoletes:	exim
Obsoletes:	masqmail
Obsoletes:	omta
Obsoletes:	qmail
Obsoletes:	sendmail
Obsoletes:	sendmail-cf
Obsoletes:	sendmail-doc
Obsoletes:	smail
Obsoletes:	smtpdaemon
Obsoletes:	zmailer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A secure, effective and simple way of getting mail off a system to
your mail hub. It contains no suid-binaries or other dangerous things
- no mail spool to poke around in, and no daemons running in the
background. Mail is simply forwarded to the configured mailhost.
Extremely easy configuration. WARNING: the above is all it does; it
does not receive mail, expand aliases or manage a queue. That belongs
on a mail hub with a system administrator.

%description -l pl.UTF-8
Bezpieczny, efektywny i prosty sposób przekazywania poczty z systemu
do własnego huba pocztowego. Nie zawiera suidowych binarek ani innych
niebezpiecznych rzeczy - nie ma spoola do wpychania czegokolwiek ani
demonów działających w tle. Poczta jest po prostu przekazywana do
zewnętrznego, skonfigurowanego serwera pocztowego. Skrajnie prosta
konfiguracja. UWAGA: powyższe to wszystko, co robi ten program; nie
odbiera poczty, nie rozwija aliasów ani nie zarządza kolejką. To
należy do huba pocztowego z własnym administratorem.

%prep
%setup -q -n %{name}
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
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}/mail,%{_prefix}/lib}

install ssmtp $RPM_BUILD_ROOT%{_sbindir}/ssmtp
install ssmtp.8 $RPM_BUILD_ROOT%{_mandir}/man8/ssmtp.8
install ssmtp.conf revaliases $RPM_BUILD_ROOT%{_sysconfdir}/mail
ln -sf %{_sbindir}/ssmtp $RPM_BUILD_ROOT%{_prefix}/lib/sendmail
ln -sf ssmtp $RPM_BUILD_ROOT%{_sbindir}/sendmail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TLS
%attr(755,root,root) %{_sbindir}/*
%attr(755,root,root) %{_prefix}/lib/sendmail
%dir %{_sysconfdir}/mail
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/ssmtp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/revaliases
%{_mandir}/man8/ssmtp*
