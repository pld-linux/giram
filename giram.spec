%define mver 0.1
Summary:	Giram Is Really A Modeller
Summary(pl):	Giram - modeler 3D
Name:		giram
Version:	0.1.11
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.giram.org/pub/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-3ds_acinclude.m4.patch
URL:		http://www.minet.net/giram/
Requires:	OpenGL
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	OpenGL-devel >= 3.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	Giram

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc/X11

%description
Giram is going to be a modeller, mostly designed for the Persistence
Of Vision Ray-Tracer. For now, it isn't really powerful. But I hope it
will grow rather quickly.

%description -l pl
Giram bêdzie narzêdziem do modelowania zbudowanym g³ównie do pracy z
POV-Ray'em. Na razie nie jest naprawdê potê¿ny, ale ma nadziejê, ¿e
szybko siê rozwinie.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
aclocal
%{__autoconf}
%{__automake}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure \
	--without-included-gettext

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Graphics

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Graphics

gzip -9nf AUTHORS ChangeLog NEWS README TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plug-ins
%attr(755,root,root) %{_libexecdir}/giram/plug-ins/*

%{_applnkdir}/Graphics/%{name}.desktop

%{_sysconfdir}/%{name}
%{_mandir}/man1/*

%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{mver}

%{_datadir}/%{name}/%{mver}/*.ppm
%attr(755,root,root) %{_datadir}/%{name}/%{mver}/user_install

%dir %{_datadir}/%{name}/%{mver}/modules
%attr(755,root,root) %{_datadir}/%{name}/%{mver}/modules/*.so
%attr(755,root,root) %{_datadir}/%{name}/%{mver}/modules/*.la

%{_datadir}/%{name}/%{mver}/color
%{_datadir}/%{name}/%{mver}/color_map
%{_datadir}/%{name}/%{mver}/finish
%{_datadir}/%{name}/%{mver}/normal
%{_datadir}/%{name}/%{mver}/pigment
%{_datadir}/%{name}/%{mver}/shape
%{_datadir}/%{name}/%{mver}/texture
%{_datadir}/%{name}/%{mver}/tips
