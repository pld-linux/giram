Summary:	Giram Is Really A Modeller
Summary:	Giram - modeler 3D
Name:		Giram
Version:	0.1.7
Release:	2
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Source0:	ftp://ftp.giram.org/pub/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
Patch0:		%{name}-Mesa-3.1.patch
URL:		http://www.minet.net/giram/
BuildRequires:	gnome-libs-devel
BuildRequires:	OpenGL-devel >= 3.1
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

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
%patch -p1

%build
gettextize --copy --force
aclocal
autoconf
CXXFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -fno-rtti -fno-exceptions -fno-implicit-templates"
export CXXFLAGS
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
%doc docs/Tutorial  {AUTHORS,ChangeLog,NEWS,README,TODO}.gz
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/Graphics/Giram.desktop
%dir %{_libexecdir}/giram
%dir %{_libexecdir}/giram/plug-ins
%attr(755,root,root) %{_libexecdir}/giram/plug-ins/*
