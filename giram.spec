Summary:	Giram Is Really A Modeller
Summary(pl):	Giram - modeler 3D
Name:		giram
Version:	0.1.11
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.giram.org/pub/giram-%{version}.tar.bz2
Source1:	%{name}.desktop
URL:		http://www.minet.net/giram/
Requires:	OpenGL
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	OpenGL-devel >= 3.1
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
Giram is going to be a modeller, mostly designed for the Persistence
Of Vision Ray-Tracer. For now, it isn't really powerful. But I hope it
will grow rather quickly.

%description -l pl
Giram b�dzie narz�dziem do modelowania zbudowanym g��wnie do pracy z
POV-Ray'em. Na razie nie jest naprawd� pot�ny, ale ma nadziej�, �e
szybko si� rozwinie.

%prep
%setup -q

%build
gettextize --copy --force
#aclocal
#autoconf
#automake -a -c
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions -fno-implicit-templates"
%configure2_13 \
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
%doc docs/Tutorial  {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*

%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plug-ins
%attr(755,root,root) %{_libexecdir}/giram/plug-ins/*

%{_applnkdir}/Graphics/%{name}.desktop

%{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/*
