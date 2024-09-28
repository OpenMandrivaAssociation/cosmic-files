%undefine _debugsource_packages
%define         appname com.system76.CosmicFiles
Name:           cosmic-files
Version:        1.0.0
Release:        0.alpha2.0
Summary:        COSMIC file manager
Group:          Utility/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-files
Source0:        https://github.com/pop-os/cosmic-files/archive/epoch-%{version}-alpha.2/%{name}-epoch-%{version}-alpha.2.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  hicolor-icon-theme
BuildRequires:  git
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(xkbcommon)

%description
File manager for the COSMIC desktop environment

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.2 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
# Build failure workaround: https://github.com/pop-os/cosmic-files/issues/392#issuecomment-2308954953
export VERGEN_GIT_COMMIT_DATE="$(date --utc '+%Y-%m-%d %H:%M:%S %z')"
export VERGEN_GIT_SHA=$_commit
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
