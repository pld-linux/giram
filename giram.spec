Summary:	Giram Is Really A Modeller
Summary(pl):	Giram - modeler 3D
Name:		giram
Version:	0.3.5
Release:	3
License:	GPL
Group:		X11/Applications/Graphics
#Source0Download: http://www.giram.org/index.php?p_menu=download
Source0:	http://www.giram.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	1197134bd838669f202fc2f2f1b5da9b
Source1:	%{name}.desktop
Patch0:		%{name}-am.patch
Patch1:		%{name}-locale-names.patch
Patch2:		%{name}-gtk.patch
Patch3:		%{name}-po.patch
URL:		http://www.giram.org/
BuildRequires:	OpenGL-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.4.0
BuildRequires:	intltool
BuildRequires:	lib3ds-devel >= 1.0.0
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	OpenGL
Obsoletes:	Giram
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		mver		0.3

%description
Giram is going to be a modeller, mostly designed for the Persistence
Of Vision Ray-Tracer. For now, it isn't really powerful. But I hope it
will grow rather quickly.

%description -l pl
Giram bêdzie narzêdziem do modelowania zbudowanym g³ównie do pracy z
POV-Rayem. Na razie nie jest naprawdê potê¿ny, ale ma nadziejê, ¿e
szybko siê rozwinie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

mv -f po/{no,nb}.po

%build
glib-gettextize --copy --force
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	POVRAY="/usr/bin/povray" \
	--disable-static \
	--enable-bishop-s3d

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/%{mver}/modules/*.la

# Greek translation is bogus here
rm -fr $RPM_BUILD_ROOT%{_datadir}/locale/el
%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog IDEAS NEWS README TODO docs/Tutorial
%lang(fr) %doc docs/Tutorial.fr
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plug-ins
%attr(755,root,root) %{_libexecdir}/giram/plug-ins/*
%dir %{_libdir}/%{name}/%{mver}
%dir %{_libdir}/%{name}/%{mver}/modules
%attr(755,root,root) %{_libdir}/%{name}/%{mver}/modules/*.so

%{_desktopdir}/%{name}.desktop

%{_sysconfdir}/%{name}
%{_mandir}/man1/*

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{mver}
%{_datadir}/%{name}/%{mver}/*.ppm
%attr(755,root,root) %{_datadir}/%{name}/%{mver}/user_install
%{_datadir}/%{name}/%{mver}/color
%{_datadir}/%{name}/%{mver}/color_map
%{_datadir}/%{name}/%{mver}/finish
%{_datadir}/%{name}/%{mver}/normal
%{_datadir}/%{name}/%{mver}/pigment
%{_datadir}/%{name}/%{mver}/shape
%{_datadir}/%{name}/%{mver}/texture
%{_datadir}/%{name}/%{mver}/tips
