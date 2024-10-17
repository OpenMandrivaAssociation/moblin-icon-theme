Name:           moblin-icon-theme
Version:        0.9
Release:        %mkrel 2
Summary:        Base moblin icons
Group:          Graphics
License:        CC-BY
BuildArch:      noarch
URL:            https://www.moblin.org
Source0:        http://git.moblin.org/cgit.cgi/%{name}/snapshot/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  hicolor-icon-theme
BuildRequires:  icon-naming-utils

%description
Contains the base icon theme for the Moblin UX

%prep
%setup -q -n %{name}-%{version}

%build
./create-icon-theme.sh moblin
cd output/moblin
autoreconf -fi
%configure
%make

%install
cd output/moblin
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_datadir}/icons/moblin


%changelog
* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9-2mdv2011.0
+ Revision: 612906
- the mass rebuild of 2010.1 packages

* Fri Nov 06 2009 Caio Begotti <caio1982@mandriva.org> 0.9-1mdv2010.1
+ Revision: 461931
- new upstream release

* Wed Oct 28 2009 Olivier Blin <oblin@mandriva.com> 0.8-1mdv2010.0
+ Revision: 459751
- 0.8 (from Caio Begotti)

* Wed Sep 30 2009 Olivier Blin <oblin@mandriva.com> 0.7-1mdv2010.0
+ Revision: 451660
- fix group
- remove useless requires
- remove scriptlets duplicate with filetriggers
- use make macro
- initial import (from Claudio Matsuoka and Caio Begotti, based on Fedora package)
- Created package structure for moblin-icon-theme.

