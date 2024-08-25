%define         appname com.system76.CosmicFiles
Name:           cosmic-files
Version:        1.0.0
Release:        0.alpha1.0
Summary:        COSMIC file manager
Group:          Utility/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-files
Source0:        https://github.com/pop-os/cosmic-files/archive/epoch-%{version}-alpha.1/%{name}-epoch-%{version}-alpha.1.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xkbcommon)

%description
File manager for the COSMIC desktop environment

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.1 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{appname}.desktop
%{_datadir}/icons/hicolor/*/apps/%{appname}.svg
%{_datadir}/metainfo/%{appname}.metainfo.xml