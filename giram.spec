Summary:	Giram Is Really A Modeller
Summary:	Giram - modeler 3D
Name:		Giram
Version:	0.0.16
Release:	1
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.minet.net/pub/giram/%{name}-%{version}.tar.bz2
URL:		http://www.minet.net/giram/
BuildRequires:	gtk+-devel >= 1.1.7
BuildRequires:	glib-devel
BuildRequires:	Mesa-devel
BuildRequires:	gettext
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix /usr/X11R6

%description
Giram is going to be a modeller, mostly designed for the Persistence Of
Vision Ray-Tracer. For now, it isn't really powerful.  But I hope it will
grow rather quickly.

%prep
%setup -q

%build
gettextize --copy --force
mkdir aclocal
cp /usr/share/aclocal/{gettext,lcmessage,progtest}.m4 aclocal
autoconf
CFLAGS="$RPM_OPT_FLAGS \
	-DHELPFILE=%{_defaultdocdir}/Giram-%{version}/Tutorial \
	-DPLUGINS_DIR=%{_datadir}/Giram/" \
	LDFLAGS="-s" \
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates" \
./configure \
	--prefix=%{_prefix} \
	--without-included-gettext
make	plugindir=%{_libdir}/Giram

%install
rm -rf $RPM_BUILD_ROOT

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	docsdir=%{_defaultdocdir}/Giram-%{version} \
	plugindir=%{_libdir}/Giram

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/Tutorial  {AUTHORS,ChangeLog,NEWS,README,TODO}.gz

%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/Giram
%attr(755,root,root) %{_libdir}/Giram/*
