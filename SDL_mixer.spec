Summary:	Simple DirectMedia Layer - Sample Mixer Library
Summary(pl):	Prosta biblioteka miksera
Summary(pt_BR):	SDL - Biblioteca para mixagem
Name:		SDL_mixer
Version:	1.2.3
Release:	2
License:	LGPL
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_mixer/release/%{name}-%{version}.tar.gz
Patch0:		%{name}-timidity_cfg.patch
URL:		http://www.libsdl.org/projects/SDL_mixer/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libSDL_mixer1.2

%define		_prefix		/usr/X11R6

%description
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%description -l es
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%description -l pl
Prosty wielo-kana�owy mikser audio. Wspiera on 4 kana�y 16 bitowego
dzwi�ku stereo plus jeden kana� dla muzyki miksowanej przez popularny
MikMod MOD, Timitity MIDI i biblioteki SMPEG MP3.

%description -l pt_BR
Biblioteca que suporta 4 canais de �udio est�reo 16 bit, mais um canal
de m�sica, mixado pelo populares bibliotecas MOD MikMod, MIDI timidity
e SMPEG MP3.

%package devel
Summary:	Header files and more to develop SDL_mixer applications
Summary(pl):	Pliki nag��wkowe do rozwoju aplikacji u�ywaj�cych SDL_mixer
Summary(pt_BR):	Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	SDL-devel
Requires:	libvorbis-devel
Obsoletes:	libSDL_mixer1.2-devel

%description devel
Header files and more to develop SDL_mixer applications.

%description devel -l es
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%description devel -l pt_BR
Bibliotecas e arquivos de inclus�o para desenvolvimento de aplica��es
SDL.

%description devel -l pl
Pliki nag��wkowe do rozwoju aplikacji u�ywaj�cych SDL_mixer

%package static
Summary:	Static SDL_mixer libraries
Summary(pl):	Statyczne biblioteki SDL_mixer
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com SDL_mixer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static SDL_mixer libraries.

%description static -l pl
Statyczne biblioteki SDL_mixer.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com SDL_mixer.

%prep
%setup -q
%patch -p1

%build
rm -f missing
libtoolize --copy --force
aclocal
autoconf
automake -a -c -f
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/playmus
%attr(755,root,root) %{_bindir}/playwave
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {README,CHANGES}.gz
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/SDL/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
