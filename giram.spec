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
BuildPrereq:	gtk+-devel >= 1.1.7
BuildPrereq:	glib-devel
BuildPrereq:	Mesa-devel
BuildPrereq:	gettext
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

%changelog
* Tue May 11 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.0.16-1]
- now package is FHS 2.0 compliant (dok moved to %{_defaultdocdir} and plugins
  to /usr/X11R6/lib/Giram/,
- recompiled on new rpm.

* Sun Apr 25 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.0.14-2]
- added BuildPrereq  rules,
- recompiled on new rpm.

* Tue Apr 13 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.0.14-1]
- added Giram plug-ins to %files.

* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.0.9-1]
- first release in rpm package.
