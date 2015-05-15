#
# Conditional build:
%bcond_without	static_libs	# don't build static libraries
#
Summary:	Open Input Framework Frame Library
Name:		frame
Version:	2.5.0
Release:	1
License:	GPL v3 / LGPL v3
Group:		Libraries
Source0:	https://launchpad.net/frame/trunk/v%{version}/+download/%{name}-%{version}.tar.xz
# Source0-md5:	f523283e80a1de613bd38e3b7f0c5f8e
URL:		https://launchpad.net/frame
BuildRequires:	asciidoc
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-xserver-server-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.6.0
BuildRequires:	xorg-proto-inputproto-devel >= 2.2.0
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Frame handles the buildup and synchronization of a set of simultaneous
touches.

%package tools
Summary:	Test tools for frame library
Summary(pl.UTF-8):	Testowe narzędzia biblioteki frame
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tools
Test tools for frame library.

%description tools -l pl.UTF-8
Testowe narzędzia biblioteki frame.

%package devel
Summary:	Header files for frame library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki frame
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for frame library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki frame.

%package static
Summary:	Static frame library
Summary(pl.UTF-8):	Statyczna biblioteka frame
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static frame library.

%description static -l pl.UTF-8
Statyczna biblioteka frame.

%prep
%setup -q

%build
%configure \
	%{!?with_static_libs:--disable-static}
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_libdir}/libframe.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libframe.so.6

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/frame-test-x11
%{_mandir}/man1/frame-test-x11.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libframe.so
%{_includedir}/oif
%{_pkgconfigdir}/frame.pc
%{_pkgconfigdir}/frame-x11.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libframe.a
%endif
