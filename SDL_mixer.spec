#
# Conditional build:
%bcond_with	modplug	# use modplug for MOD support (mikmod is used by default)
#
# NOTE: libraries dlopened by sonames detected at build time:
# libFLAC.so.8
# libfluidsynth.so.1
# libmikmod.so.2
# libsmpeg-0.4.so.0
# libvorbisfile.so.3
#
Summary:	Simple DirectMedia Layer - Sample Mixer Library
Summary(pl.UTF-8):	Simple DirectMedia Layer - biblioteka miksująca próbki dźwiękowe
Summary(pt_BR.UTF-8):	SDL - Biblioteca para mixagem
Name:		SDL_mixer
Version:	1.2.12
Release:	4
License:	Zlib-like
Group:		Libraries
Source0:	http://www.libsdl.org/projects/SDL_mixer/release/%{name}-%{version}.tar.gz
# Source0-md5:	e03ff73d77a55e3572ad0217131dc4a1
Patch0:		%{name}-timidity_cfg.patch
Patch1:		%{name}-acfix.patch
Patch2:		%{name}-link.patch
URL:		http://www.libsdl.org/projects/SDL_mixer/release-1.2.html
BuildRequires:	SDL-devel >= 1.2.10
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.2.0
BuildRequires:	fluidsynth-devel
BuildRequires:	libtool >= 2:2.0
BuildRequires:	libmikmod-devel >= 3.1.10
%{?with_modplug:BuildRequires:	libmodplug-devel >= 0.8.7}
BuildRequires:	libvorbis-devel >= 1:1.0
BuildRequires:	smpeg-devel >= 0.4.4-11
Requires:	SDL >= 1.2.10
%{?with_modplug:Suggests:	libmodplug >= 0.8.7}
Obsoletes:	libSDL_mixer1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Due to popular demand, here is a simple multi-channel audio mixer. It
supports 4 channels of 16 bit stereo audio, plus a single channel of
music, mixed by the popular MikMod MOD, Timidity MIDI and SMPEG MP3
libraries.

%description -l pl.UTF-8
SDL_mixer to prosty wielokanałowy mikser audio. Obsługuje 4 kanały
16-bitowego dźwięku stereo plus jeden kanał dla muzyki miksowanej
przez popularne biblioteki MikMod MOD, Timitity MIDI i SMPEG MP3.

%description -l pt_BR.UTF-8
Biblioteca que suporta 4 canais de áudio estéreo 16 bit, mais um canal
de música, mixado pelo populares bibliotecas MOD MikMod, MIDI timidity
e SMPEG MP3.

%package devel
Summary:	Header files and more to develop SDL_mixer applications
Summary(pl.UTF-8):	Pliki nagłówkowe do rozwoju aplikacji używających biblioteki SDL_mixer
Summary(pt_BR.UTF-8):	Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações SDL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	SDL-devel >= 1.2.10
Obsoletes:	libSDL_mixer1.2-devel

%description devel
Header files and more to develop SDL_mixer applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe do rozwoju aplikacji używających biblioteki
SDL_mixer.

%description devel -l pt_BR.UTF-8
Bibliotecas e arquivos de inclusão para desenvolvimento de aplicações
SDL.

%package static
Summary:	Static SDL_mixer library
Summary(pl.UTF-8):	Statyczna biblioteka SDL_mixer
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com SDL_mixer
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static SDL_mixer library.

%description static -l pl.UTF-8
Statyczna biblioteka SDL_mixer.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com SDL_mixer.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%configure \
	%{?with_modplug:--enable-music-mod-modplug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-bin \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libSDL_mixer.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CHANGES COPYING README
%attr(755,root,root) %{_bindir}/playmus
%attr(755,root,root) %{_bindir}/playwave
%attr(755,root,root) %{_libdir}/libSDL_mixer-1.2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libSDL_mixer-1.2.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libSDL_mixer.so
%{_includedir}/SDL/SDL_mixer.h
%{_pkgconfigdir}/SDL_mixer.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libSDL_mixer.a
