#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	Yubikey management library and client
Summary(pl.UTF-8):	Biblioteka i klient do zarządzania urządzeniami Yubikey
Name:		ykclient
Version:	2.15
Release:	2
License:	BSD
Group:		Applications/System
Source0:	https://developers.yubico.com/yubico-c-client/Releases/%{name}-%{version}.tar.gz
# Source0-md5:	d7da4d4acc1461af06346e194aa4960b
URL:		https://developers.yubico.com/yubico-c-client/
BuildRequires:	curl-devel
BuildRequires:	help2man
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yubikey management library and command line client.

%description -l pl.UTF-8
Biblioteka i działający z linii poleceń klient do zarządzania
urządzeniami Yubikey.

%package devel
Summary:	Development headers for ykclient library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki ykclient
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development files for ykclient library needed to build applications to
take advantage of Yubikey authentication.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki ykclient, potrzebne przy tworzeniu
aplikacji wykorzystujących uwierzytelnianie Yubikey.

%package static
Summary:	Static ykclient library
Summary(pl.UTF-8):	Statyczna biblioteka ykclient
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static ykclient library.

%description static -l pl.UTF-8
Statyczna biblioteka ykclient.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libykclient.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ykclient
%attr(755,root,root) %{_libdir}/libykclient.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libykclient.so.3
%{_mandir}/man1/ykclient.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libykclient.so
%{_includedir}/ykclient*.h

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libykclient.a
%endif
