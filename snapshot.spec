## Workaround for empty debug
%define _empty_manifest_terminate_build 0

%global tarball_version %%(echo %{version} | tr '~' '.')
 
Name:           snapshot
Version:        46.2
Release:        1
Summary:        Take pictures and videos
License:        GPL-3.0-or-later
URL:            https://gitlab.gnome.org/GNOME/snapshot
Source0:        https://download.gnome.org/sources/snapshot/45/snapshot-%{tarball_version}.tar.xz

BuildRequires:  meson
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  gettext
BuildRequires:  appstream < 1.0.0
BuildRequires:  appstream-util
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
## for camerabin
BuildRequires:  pkgconfig(gstreamer-plugins-bad-1.0)
BuildRequires:  pkgconfig(gstreamer-video-1.0)
## For hicolor icon theme directories
Requires:       hicolor-icon-theme

Provides:       bundled(crate(aperture)) = 0.3.1
 
%description
Take pictures and videos on your computer, tablet, or phone.
 
 
%prep
%autosetup -n snapshot-%{tarball_version} a2 -p1

## needed only if we use own vendored dependencies
#mkdir .cargo
#cp %{SOURCE3} .cargo/config
 
%build
%meson
%meson_build
 
%install
%meson_install
%find_lang snapshot --with-gnome
 
%files -f snapshot.lang
%license LICENSE
%doc README.md
%{_bindir}/snapshot
%{_datadir}/applications/org.gnome.Snapshot.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.Snapshot.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Snapshot*.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Snapshot-symbolic.svg
%{_datadir}/snapshot/
%{_metainfodir}/org.gnome.Snapshot.metainfo.xml
