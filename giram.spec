Summary:	Giram Is Really A Modeller
Summary:	Giram - modeler 3D
Name:		Giram
Version:	0.0.12
Release:	1
Copyright:	GPL
Group:		X11/Applications/Graphics
Group(pl):	X11/Aplikacje/Grafika
Source:		ftp://ftp.minet.net/pub/giram/%{name}-%{version}.tar.bz2
Patch:		Giram-DESTDIR.patch
URL:		http://www.minet.net/giram/
BuildPrereq:	gtk+-devel >= 1.1.7
BuildPrereq:	glib-devel
%requires_pkg	gtk+
%requires_pkg	glib
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Giram is going to be a modeller, mostly designed for the Persistence Of
Vision Ray-Tracer. For now, it isn't really powerful.  But I hope it will
grow rather quickly.


%prep
%setup -q
%patch -p1

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure \
	--prefix=/usr/X11R6 \
	--without-included-gettext
make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(755,root,root) /usr/X11R6/bin/*

%lang(fr) /usr/X11R6/share/locale/fr/LC_MESSAGES/giram.mo

%changelog
* Mon Jan 04 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [0.0.9-1]
- first release in rpm package.
