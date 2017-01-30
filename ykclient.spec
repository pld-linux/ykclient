Summary:	Yubikey management library and client
Name:		ykclient
Version:	2.15
Release:	1
License:	BSD
Group:		Applications/System
URL:		http://opensource.yubico.com/yubico-c-client/
Source0:	http://opensource.yubico.com/yubico-c-client/releases/%{name}-%{version}.tar.gz
# Source0-md5:	d7da4d4acc1461af06346e194aa4960b
BuildRequires:	chrpath
BuildRequires:	curl-devel
BuildRequires:	help2man
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Commandline for yubikeys.

%package devel
Summary:	Development headers and libraries for ykclient
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
development files for ykclient needed to build applications to take
advantage of yubikey authentication.

%prep
%setup -q

%build
%configure \
	--disable-static \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_libdir}/libykclient.la
chrpath -d $RPM_BUILD_ROOT%{_bindir}/ykclient

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_bindir}/ykclient
%attr(755,root,root) %ghost %{_libdir}/libykclient.so.3
%attr(755,root,root) %{_libdir}/libykclient.so.*.*
%{_mandir}/man1/ykclient.1*

%files devel
%defattr(644,root,root,755)
%doc README NEWS AUTHORS
%{_includedir}/*.h
%attr(755,root,root) %{_libdir}/libykclient.so
