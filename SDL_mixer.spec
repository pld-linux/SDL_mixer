Summary:	Simple DirectMedia Layer - Sample Mixer Library
Summary(pl):	Prosta biblioteka miksera
Name:		SDL_mixer
Version:	1.1.0
Release:	4
License:	LGPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	http://www.libsdl.org/projects/SDL_mixer/src/%{name}-%{version}.tar.gz
Patch0:		%{name}-timidity_cfg.patch
URL:		http://www.libsdl.org/projects/SDL_mixer/index.html
BuildRequires:	esound-devel
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%description -l pl
Prosty wielo-kana�owy mikser audio. Wspiera on 4 kana�y 16 bitowego
dzwi�ku stereo plus jeden kana� dla muzyki miksowanej przez popularny
MikMod MOD, Timitity MIDI i biblioteki SMPEG MP3.

%package devel
Summary:	Header files and more to develop SDL_mixer applications
Summary(pl):	Pliki nag�owkowe do rozwoju aplikacji u�ywaj�cych SDL_mixer
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}
Requires:	SDL-devel

%description devel
Header files and more to develop SDL_mixer applications.

%description -l pl devel
Pliki nag�owkowe do rozwoju aplikacji u�ywaj�cych SDL_mixer

%package static
Summary:	Static SDL_mixer libraries
Summary(pl):	Statyczne biblioteki SDL_mixer
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Statis SDL_mixer libraries.

%description -l pl static
Statyczne biblioteki SDL_mixer.

%prep
%setup -q 
%patch -p1

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/playmus
%attr(755,root,root) %{_bindir}/playwave
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
