Summary:	Free AudioGalaxy Satellite client.
Name:		fags
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Multimedia
######		Unknown group!
Source0:	ftp://ftp.tty0.org/pub/fags/%{name}-%{version}.tar.gz
Patch0:		%{name}-config_dir.patch
URL:		http://www.tty0.org/page/fags 
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
FAGS is a Free AudioGalaxy Satellite client for UNIX and Linux. It is
written in C and licensed under the GNU General Public License.

FAGS features up to 20 simultaneous uploads or downloads using
asynchronous socket I/O, resuming of uploads and downloads, sharing of
multiple directories, reading of MP3 and OGG Vorbis ID3 tags and
bandwidth limiting.

%prep
%setup -q
%patch0 -p1

%build
aclocal
automake -a -c
autoconf
%configure
%__make

%install
rm -rf $RPM_BUILD_ROOT
rm -rf %{buildroot}
%__make install  DESTDIR=$RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/*