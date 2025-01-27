%define name photopc
%define version 3.05
%define release %mkrel 11

Summary: Digital camera image downloader
Name: %{name}
Version: %{version}
Release: %{release}
License: Distributable
URL: https://www.average.org/digicam/
Group: Graphics
Source: %{name}-%{version}.tar.bz2
Buildroot: %{_tmppath}/%{name}-buildroot

%description
This is a library and a command-line frontend to manipulate digital
still cameras based on Fujitsu chipset and Sierra Imaging firmware.  The
program is known to work with Agfa, Epson, Olympus, Sanyo and Nikon (at
least CoolPix 900, but not CoolPix 600!) cameras.

The cameras typically come with software for Windows and for Mac, and no
description of the protocol.  With this tool, they are manageable from a
UNIX box.  Bruce D. Lightner <lightner@lightner.net> has added support
for Win32 and DOS platforms.  Note that the program does not have any
GUI, it is plain command-line even on Windows.

%package -n %name-devel
Summary: Digital camera image downloader, devel files
Group: Development/Other


%description -n %name-devel
This is a library and a command-line frontend to manipulate digital
still cameras based on Fujitsu chipset and Sierra Imaging firmware.  The
program is known to work with Agfa, Epson, Olympus, Sanyo and Nikon (at
least CoolPix 900, but not CoolPix 600!) cameras.

The cameras typically come with software for Windows and for Mac, and no
description of the protocol.  With this tool, they are manageable from a
UNIX box.  Bruce D. Lightner <lightner@lightner.net> has added support
for Win32 and DOS platforms.  Note that the program does not have any
GUI, it is plain command-line even on Windows.


%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build

%configure

%make

%install

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README protocol.htm usage.htm
%{_bindir}/*
%{_mandir}/man*/*

%files -n %name-devel
%defattr(-,root,root)
%_includedir/*
%_libdir/*




%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 3.05-11mdv2010.0
+ Revision: 430688
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.05-10mdv2009.0
+ Revision: 258992
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tvignaud@mandriva.com> 3.05-9mdv2009.0
+ Revision: 246863
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 3.05-7mdv2008.1
+ Revision: 136373
- restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request


* Thu Nov 23 2006 Lenny Cartier <lenny@mandriva.com> 3.05-7mdv2007.0
+ Revision: 86780
- Use mkrel
- Import photopc

