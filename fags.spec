Summary:	Free AudioGalaxy Satellite client
Summary(pl):	"Wolny" klient AudioGalaxy
Name:		fags
Version:	0.2.1
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	ftp://ftp.tty0.org/pub/fags/%{name}-%{version}.tar.gz
# Source0-md5:	5ce2f79e63fa49138cf7374a68f611dd
Patch0:		%{name}-config_dir.patch
URL:		http://www.tty0.org/page/fags/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
FAGS is a Free AudioGalaxy Satellite client for UNIX and Linux. It is
written in C and licensed under the GNU General Public License.

FAGS features up to 20 simultaneous uploads or downloads using
asynchronous socket I/O, resuming of uploads and downloads, sharing of
multiple directories, reading of MP3 and OGG Vorbis ID3 tags and
bandwidth limiting.

%description -l pl
FAGS jest "wolnym" klientem AudioGalaxy dla UNIKSA i Linuksa. Zosta³
napisany w C i wydany na licencji GNU General Public License.

FAGS umo¿liwia do 20 równoczesnych przekazów lub pobrañ u¿ywaj±c
asynchronicznych gniazd WE/WY. Wspiera tak¿e wznawianie transmisji,
dzielenie wielokrotnych katalogów, odczyt tagów ID3 z plików MP3 i OGG
Vorbis oraz ograniczanie szeroko¶ci pasma.

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__automake}
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README TODO doc/*
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
