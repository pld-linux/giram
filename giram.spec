Summary:	Giram Is Really A Modeller
Summary:	Giram - modeler 3D
Name:		Giram
Version:	0.1.4
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.minet.net/pub/giram/%{name}-%{version}.tar.bz2
URL:		http://www.minet.net/giram/
BuildRequires:	gtk+-devel >= 1.1.7
BuildRequires:	glib-devel
BuildRequires:	Mesa-devel >= 3.1
BuildRequires:	gettext-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix		/usr/X11R6

%description
Giram is going to be a modeller, mostly designed for the Persistence Of
Vision Ray-Tracer. For now, it isn't really powerful.  But I hope it will
grow rather quickly.

%prep
%setup -q

%build
gettextize --copy --force
aclocal
autoconf
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -fno-rtti -fno-exceptions -fno-implicit-templates"
CXXFLAGS="$RPM_OPT_FLAGS"
export LDFLAGS CXXFLAGS
%configure \
	--without-included-gettext

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc docs/Tutorial  {AUTHORS,ChangeLog,NEWS,README,TODO}.gz

%attr(755,root,root) %{_bindir}/*
%dir %{_libexecdir}/giram
%dir %{_libexecdir}/giram/plug-ins
%attr(755,root,root) %{_libexecdir}/giram/plug-ins/*
