Summary:	Extremely simple MTA to get mail off the system to a mail hub
Summary(pl.UTF-8):	Skrajnie prosty MTA do przekazywania poczty z systemu do huba
Name:		ssmtp
Version:	2.64
Release:	9
License:	GPL
Group:		Networking/Daemons/SMTP
Source0:	http://http.us.debian.org/debian/pool/main/s/ssmtp/%{name}_%{version}.orig.tar.bz2
# Source0-md5:	65b4e0df4934a6cd08c506cabcbe584f
Patch0:		%{name}-nonsl.patch
Patch1:		%{name}-ssl.patch
Patch2:		%{name}-garbage_writes.patch
Patch3:		%{name}-authpass.patch
Patch4:		%{name}-validate-TLS-server-cert.patch
Patch5:		defaultvalues.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	openssl-devel
Requires:	%{name}-base = %{version}-%{release}
Provides:	smtpdaemon
Obsoletes:	smtpdaemon
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

%package base
Summary:	Extremely simple MTA to get mail off the system to a mail hub
Summary(pl.UTF-8):	Skrajnie prosty MTA do przekazywania poczty z systemu do huba
Group:		Networking/Daemons/SMTP

%description base
A secure, effective and simple way of getting mail off a system to
your mail hub. It contains no suid-binaries or other dangerous things
- no mail spool to poke around in, and no daemons running in the
  background. Mail is simply forwarded to the configured mailhost.
  Extremely easy configuration. WARNING: the above is all it does; it
  does not receive mail, expand aliases or manage a queue. That belongs
  on a mail hub with a system administrator.

%description base -l pl.UTF-8
Bezpieczny, efektywny i prosty sposób przekazywania poczty z systemu
do własnego huba pocztowego. Nie zawiera suidowych binarek ani innych
niebezpiecznych rzeczy - nie ma spoola do wpychania czegokolwiek ani
demonów działających w tle. Poczta jest po prostu przekazywana do
zewnętrznego, skonfigurowanego serwera pocztowego. Skrajnie prosta
konfiguracja. UWAGA: powyższe to wszystko, co robi ten program; nie
odbiera poczty, nie rozwija aliasów ani nie zarządza kolejką. To
należy do huba pocztowego z własnym administratorem.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1
%patch -P4 -p1
%patch -P5 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%configure2_13 \
	--enable-ssl

%{__make} \
	SSMTPCONFDIR=%{_sysconfdir}/mail

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{5,8},%{_sysconfdir}/mail,/usr/lib}

install ssmtp $RPM_BUILD_ROOT%{_sbindir}/ssmtp
install ssmtp.8 $RPM_BUILD_ROOT%{_mandir}/man8/ssmtp.8
install ssmtp.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/ssmtp.conf.5
install ssmtp.conf revaliases $RPM_BUILD_ROOT%{_sysconfdir}/mail
ln -sf %{_sbindir}/ssmtp $RPM_BUILD_ROOT/usr/lib/sendmail
ln -sf ssmtp $RPM_BUILD_ROOT%{_sbindir}/sendmail

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/sendmail
%attr(755,root,root) /usr/lib/sendmail

%files base
%defattr(644,root,root,755)
%doc README TLS
%attr(755,root,root) %{_sbindir}/ssmtp
%dir %{_sysconfdir}/mail
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/ssmtp.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/mail/revaliases
%{_mandir}/man8/ssmtp.8*
%{_mandir}/man5/ssmtp.conf.5*
