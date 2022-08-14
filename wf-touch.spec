%define git 20210319

Name:           wf-touch
Version:        0.0
Release:        1.%{git}.1
Summary:        Touchscreen gesture library
Group:          Wayfire
License:        MIT
URL:            https://github.com/WayfireWM/wf-touch
# There is no release or tags yet. So for now use master branch
Source0:        https://github.com/WayfireWM/wf-touch/archive/refs/heads/wf-touch-master.tar.gz
 
BuildRequires:  cmake
BuildRequires:  meson
 
%description
Touchscreen gesture library

Acknowledgements
The library's design has been heavily inspired by https://github.com/grahnen/libtouch, 
which has also been used as a reference for some implementation details at times.
 
%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
 
%description    devel
Development files for %{name}.
 
%prep
%autosetup -n %{name}-master -p1
 

%build
%meson \
    -Dtests=disabled
 
%meson_build
 
%install
%meson_install
 
%files
