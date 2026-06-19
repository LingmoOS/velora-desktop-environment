Name:           deepin-desktop-environment
Version:        1.0.0
Release:        1%{?dist}
Summary:        Lingmo Desktop Environment (Meta Package)
License:        GPL-3.0-or-later
URL:            https://github.com/LingmoOS/desktop-environment

# Meta package - no source tarball needed
%description
Meta package providing the complete Lingmo desktop environment.
This package depends on all core components of the Lingmo desktop.

%prep
# No source to prepare

%build
# Nothing to build

%install
mkdir -p %{buildroot}%{_datadir}/deepin-desktop-environment/

%files
%doc README.md
%license LICENSE*
%{_datadir}/deepin-desktop-environment/

%changelog
* Tue Jun 18 2025 LingmoOS Build System <dev@lingmo.os> - %{version}-1
- Initial RPM packaging for local source build
