Name:           moblin-icon-theme
Version:        0.7
Release:        %mkrel 1
Summary:        Base moblin icons

Group:          Graphics
License:        CC-BY
BuildArch:      noarch
URL:            http://www.moblin.org
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
